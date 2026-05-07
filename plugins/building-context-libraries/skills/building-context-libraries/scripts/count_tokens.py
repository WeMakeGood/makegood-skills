#!/usr/bin/env python3
"""
Count tokens in context library modules and calculate agent budgets.

The per-agent module budget is 10% of the target model's context window.
Addenda are excluded from token counts — they are loaded on demand.

Usage:
    python count_tokens.py <library_dir> [agents_dir] [--context-window N]

Examples:
    python count_tokens.py ./modules ./agents
    python count_tokens.py ./modules ./agents --context-window 200000
"""

import sys
import argparse
import yaml
from pathlib import Path


DEFAULT_CONTEXT_WINDOW = 200000  # Claude Sonnet 4.5
BUDGET_PERCENTAGE = 0.10  # 10% of context window


def estimate_tokens(text: str) -> int:
    """Estimate tokens (roughly 0.75 words per token for English)."""
    words = len(text.split())
    return int(words / 0.75)


def parse_frontmatter(content: str) -> tuple:
    """Extract YAML frontmatter and body from markdown."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
                body = parts[2]
                return frontmatter, body
            except yaml.YAMLError:
                pass
    return {}, content


def analyze_module(filepath: Path) -> dict:
    """Analyze a single module file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        return {
            'path': str(filepath),
            'name': filepath.stem,
            'module_id': frontmatter.get('module_id', filepath.stem),
            'module_name': frontmatter.get('module_name', filepath.stem),
            'tier': frontmatter.get('tier', 'unknown'),
            'tokens': estimate_tokens(content),
            'error': None
        }
    except Exception as e:
        return {
            'path': str(filepath),
            'name': filepath.stem,
            'error': str(e)
        }


HARD_RULE_ALWAYS_LOAD = {'F0_agent_behavioral_standards', 'S0_natural_prose_standards'}


def analyze_agent(filepath: Path) -> dict:
    """Analyze an agent definition file using the always_load/conditional manifest format.

    Returns a dict with the agent's classified items, or an error if the manifest
    is in the pre-1.5 format and needs migration.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = parse_frontmatter(content)

        # Detect old-format manifests and refuse with a migration pointer.
        if 'modules' in frontmatter and 'always_load' not in frontmatter:
            modules_field = frontmatter.get('modules')
            if isinstance(modules_field, dict) and any(
                k in modules_field for k in ('foundation', 'shared', 'specialized')
            ):
                return {
                    'path': str(filepath),
                    'name': frontmatter.get('agent_name', filepath.stem),
                    'error': (
                        "Pre-1.5 manifest format (tier-grouped modules:/addenda:). "
                        "This library needs migration before token counting will be accurate. "
                        "See references/phases/PHASE_M_MIGRATION.md."
                    ),
                    'needs_migration': True,
                }

        # New-format parsing.
        always_load = frontmatter.get('always_load', []) or []
        conditional_raw = frontmatter.get('conditional', []) or []

        # Conditional items are dicts with module:/addendum: + load_when:.
        # We only need item names for budget purposes; conditional doesn't count.
        conditional_items = []
        for entry in conditional_raw:
            if isinstance(entry, dict):
                # Pick whichever key is present (module or addendum).
                name = entry.get('module') or entry.get('addendum') or ''
                if name:
                    conditional_items.append(name)

        # F0/S0 hard-rule check: if either appears in conditional, refuse.
        violations = []
        for name in conditional_items:
            base = name.split('/')[-1]  # strip any path prefix
            if base in HARD_RULE_ALWAYS_LOAD:
                violations.append(base)

        if violations:
            return {
                'path': str(filepath),
                'name': frontmatter.get('agent_name', filepath.stem),
                'error': (
                    f"Hard-rule violation: {', '.join(violations)} appears in `conditional`. "
                    "F0_agent_behavioral_standards and S0_natural_prose_standards are always_load "
                    "whenever they appear in an agent's set. See SKILL.md, Critical Rules."
                ),
                'hard_rule_violation': True,
            }

        return {
            'path': str(filepath),
            'name': frontmatter.get('agent_name', filepath.stem),
            'always_load': always_load,
            'conditional': conditional_items,
            'stated_tokens': frontmatter.get('estimated_tokens'),
            'error': None,
        }
    except Exception as e:
        return {
            'path': str(filepath),
            'name': filepath.stem,
            'error': str(e)
        }


def find_modules(library_dir: Path) -> list:
    """Find all module files in library (excludes addenda)."""
    modules = []
    for subdir in ['foundation', 'shared', 'specialized']:
        subpath = library_dir / subdir
        if subpath.exists():
            modules.extend(subpath.glob('*.md'))
    return modules


def find_addenda(library_dir: Path) -> list:
    """Find all addendum files in the addenda/ tree (recursive — addenda may be in subdirs).

    Returns a flat list of Path objects. The library_dir argument here is expected to be
    the parent of `addenda/` — typically the same path passed for modules.
    """
    addenda = []
    addenda_root = library_dir.parent / 'addenda' if library_dir.name == 'modules' else library_dir / 'addenda'
    if addenda_root.exists():
        addenda.extend(addenda_root.rglob('*.md'))
    return addenda


def main():
    parser = argparse.ArgumentParser(
        description='Count tokens in context library modules and calculate agent budgets.'
    )
    parser.add_argument('library_dir',
                       help='Path to library/ folder with modules')
    parser.add_argument('agents_dir', nargs='?',
                       help='Optional path to agents/ folder')
    parser.add_argument('--context-window', type=int, default=DEFAULT_CONTEXT_WINDOW,
                       help=f'Target model context window in tokens (default: {DEFAULT_CONTEXT_WINDOW:,})')

    args = parser.parse_args()
    library_dir = Path(args.library_dir)
    agents_dir = Path(args.agents_dir) if args.agents_dir else None
    token_limit = int(args.context_window * BUDGET_PERCENTAGE)

    if not library_dir.exists():
        print(f"Error: Library directory '{library_dir}' not found")
        sys.exit(1)

    # Analyze modules
    module_files = find_modules(library_dir)
    modules = {}

    # Analyze addenda (some may be always_load and count toward budget)
    addendum_files = find_addenda(library_dir)
    addenda = {}

    print("Token Count Report")
    print("==================")
    print(f"Context window: {args.context_window:,} tokens")
    print(f"Per-agent budget: {token_limit:,} tokens (10% of context window)")
    print(f"Always-loaded items count toward budget; conditional items do not.")
    print()
    print("MODULES")
    print("-" * 60)
    print(f"{'Module ID':<30} {'Tier':<15} {'Tokens':>10}")
    print("-" * 60)

    total_tokens = 0
    for mf in sorted(module_files):
        result = analyze_module(mf)
        if result.get('error'):
            print(f"{result['name']:<30} ERROR: {result['error']}")
        else:
            modules[result['module_id']] = result
            print(f"{result['module_id']:<30} {result['tier']:<15} {result['tokens']:>10}")
            total_tokens += result['tokens']

    print("-" * 60)
    print(f"{'TOTAL':<45} {total_tokens:>10}")
    print()

    if addendum_files:
        print("ADDENDA")
        print("-" * 60)
        print(f"{'Addendum':<45} {'Tokens':>10}")
        print("-" * 60)
        for af in sorted(addendum_files):
            result = analyze_module(af)  # same parser works for addenda frontmatter
            if not result.get('error'):
                # Index by stem and by addendum_id-like fallback for matching against agent manifests.
                addenda[result['name']] = result
                print(f"{result['name']:<45} {result['tokens']:>10}")
        print("-" * 60)
        print()

    # Analyze agents if provided
    if agents_dir and agents_dir.exists():
        agent_files = list(agents_dir.glob('*.md'))

        if agent_files:
            limit_label = f"% of {token_limit // 1000}K"
            print("AGENT TOKEN BUDGETS (always-loaded items only)")
            print("-" * 70)
            print(f"{'Agent':<30} {'Tokens':>10} {limit_label:>10} {'Status':>10}")
            print("-" * 70)

            had_errors = False
            for af in sorted(agent_files):
                agent = analyze_agent(af)
                if agent.get('error'):
                    had_errors = True
                    print(f"{agent['name']:<30} ERROR")
                    print(f"  {agent['error']}")
                    continue

                # Calculate tokens from always_load items only.
                agent_tokens = 0
                missing_items = []
                for item_ref in agent['always_load']:
                    # Item refs may be bare names (F1_org_identity) or path-prefixed
                    # (reference/A0_organizational_reference). Match by stem against
                    # both modules and addenda dicts.
                    stem = item_ref.split('/')[-1]
                    matched = False
                    # Try modules first.
                    for mid, mdata in modules.items():
                        if mid == stem or mdata['name'] == stem:
                            agent_tokens += mdata['tokens']
                            matched = True
                            break
                    if not matched:
                        # Try addenda.
                        for aname, adata in addenda.items():
                            if aname == stem:
                                agent_tokens += adata['tokens']
                                matched = True
                                break
                    if not matched:
                        missing_items.append(item_ref)

                pct = (agent_tokens / token_limit) * 100
                if agent_tokens > token_limit:
                    status = "OVER"
                elif pct < 50:
                    status = "THIN"
                elif pct > 80:
                    status = "WARN"
                else:
                    status = "OK"

                conditional_count = len(agent.get('conditional', []))
                print(f"{agent['name']:<30} {agent_tokens:>10} {pct:>9.1f}% {status:>10}")
                print(f"  Conditional items: {conditional_count} (not counted)")

                if missing_items:
                    print(f"  Missing from library: {', '.join(missing_items)}")

            print("-" * 70)
            print()
            print(f"Budget: 10% of {args.context_window:,} context window = {token_limit:,} tokens per agent")
            print("Status: THIN = under 50% (likely underserved), OK = 50-80%, WARN = 80-100%, OVER = exceeds limit")
            print("Note: Conditional items (loaded only when their load_when: trigger applies) do NOT count toward budget.")

            if had_errors:
                print()
                print("WARNING: One or more agents had errors. Pre-1.5 manifests need migration; hard-rule violations need correction. See messages above.")
                sys.exit(1)

    else:
        print("No agents directory provided. Run with agents path to check budgets:")
        print(f"  python count_tokens.py {library_dir} ./agents")


if __name__ == '__main__':
    main()
