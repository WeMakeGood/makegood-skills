#!/usr/bin/env python3
"""
Extract a flat reference of all Divi 5 module attribute paths and their defaults.

Reads:
  - module.json files from each module component directory (attribute schemas)
  - _all_modules_default_printed_style_attributes.php (default values)

Outputs:
  divi-module-reference.json — a flat map of every module's settable attribute
  paths, organized by module name, element, and category.

Usage:
  python3 extract_module_reference.py
  python3 extract_module_reference.py --divi-path ./Divi
  python3 extract_module_reference.py -o custom-output.json
"""

import argparse
import json
import re
from pathlib import Path


# ── PHP array parser (minimal) ───────────────────────────────────────────────
# The defaults file is a PHP array literal. We convert it to JSON-parseable
# form rather than exec'ing PHP.

def parse_php_defaults(php_path: Path) -> dict:
    """
    Parse the _all_modules_default_printed_style_attributes.php file into a
    Python dict. Uses PHP CLI to evaluate the file and output JSON, which
    avoids the complexity of converting PHP array syntax to JSON in Python.
    Falls back to a regex-based parser if PHP is not available.
    """
    import subprocess

    # Try using PHP CLI to evaluate the file directly.
    try:
        result = subprocess.run(
            ["php", "-r", f"echo json_encode(require '{php_path}');"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout:
            return json.loads(result.stdout)
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        pass

    # Fallback: token-based conversion for environments without PHP.
    # PHP single-quoted strings can contain double quotes (unescaped), so we
    # must escape them when converting to JSON double-quoted strings.
    text = php_path.read_text()

    # Remove PHP comments.
    text = re.sub(r'//.*?\n', '\n', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)

    # Strip PHP opening and return statement.
    text = re.sub(r'^<\?php\s*', '', text, flags=re.DOTALL)
    text = re.sub(r'^return\s+', '', text.strip(), flags=re.DOTALL)
    text = re.sub(r'\];\s*$', ']', text.strip())

    # Convert PHP single-quoted strings to JSON double-quoted strings.
    # Inside PHP single quotes, only \' and \\ are escape sequences.
    # Double quotes inside are literal and must be escaped for JSON.
    def convert_php_string(match):
        content = match.group(1)
        # Unescape PHP single-quote escapes.
        content = content.replace("\\'", "'")
        content = content.replace("\\\\", "\\")
        # Escape for JSON double-quoted string.
        content = content.replace("\\", "\\\\")
        content = content.replace('"', '\\"')
        content = content.replace("\n", "\\n")
        content = content.replace("\t", "\\t")
        return f'"{content}"'

    # Match PHP single-quoted strings (handling escaped single quotes inside).
    text = re.sub(r"'((?:[^'\\]|\\.)*)'", convert_php_string, text)

    # Replace => with :
    text = text.replace('=>', ':')

    # Convert PHP [] to JSON {} for associative arrays.
    # Parse character by character, tracking whether each [] is an object or array.
    result_chars = []
    brace_stack = []
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '[':
            # Distinguish associative arrays (objects) from indexed arrays.
            # Associative: [ "key" => ...  (after conversion: [ "key" : ...)
            # Indexed:     [ "value", ... ] or [ ]
            rest = text[i+1:].lstrip()
            is_assoc = False
            if rest and rest[0] == '"':
                # Find the closing quote, then check if : follows.
                close_q = rest.find('"', 1)
                if close_q > 0:
                    after_str = rest[close_q+1:].lstrip()
                    is_assoc = after_str.startswith(':')
            if is_assoc:
                result_chars.append('{')
                brace_stack.append('object')
            else:
                result_chars.append('[')
                brace_stack.append('array')
        elif ch == ']':
            if brace_stack and brace_stack[-1] == 'object':
                result_chars.append('}')
            else:
                result_chars.append(']')
            if brace_stack:
                brace_stack.pop()
        elif ch == '"':
            # Skip over the entire string literal without modifying it.
            result_chars.append('"')
            i += 1
            while i < len(text) and text[i] != '"':
                if text[i] == '\\':
                    result_chars.append(text[i])
                    i += 1
                    if i < len(text):
                        result_chars.append(text[i])
                else:
                    result_chars.append(text[i])
                i += 1
            if i < len(text):
                result_chars.append('"')
        else:
            result_chars.append(ch)
        i += 1

    text = ''.join(result_chars)

    # Remove trailing commas.
    text = re.sub(r',\s*([}\]])', r'\1', text)

    # PHP literals.
    text = re.sub(r'\btrue\b', 'true', text)
    text = re.sub(r'\bfalse\b', 'false', text)
    text = re.sub(r'\bnull\b', 'null', text)

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"  Warning: Could not parse PHP defaults (no PHP CLI, fallback failed): {e}")
        return {}


# ── Path flattening ──────────────────────────────────────────────────────────

def flatten_paths(obj, prefix="", separator=".") -> dict:
    """
    Flatten a nested dict into dot-separated paths with leaf values.
    Example: {"a": {"b": "x"}} -> {"a.b": "x"}
    """
    result = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            new_prefix = f"{prefix}{separator}{key}" if prefix else key
            if isinstance(value, dict):
                result.update(flatten_paths(value, new_prefix, separator))
            else:
                result[new_prefix] = value
    return result


# ── Module schema extraction ─────────────────────────────────────────────────

def extract_settable_paths_from_schema(module_json: dict) -> dict:
    """
    Extract settable attribute paths from a module.json schema.

    Returns a dict keyed by element name (e.g., "module", "content", "button"),
    each containing:
      - decoration_groups: list of decoration group names (e.g., "font", "border")
      - style_props: list of style prop names
      - settings: nested structure of configurable settings
    """
    attributes = module_json.get("attributes", {})
    elements = {}

    for element_name, element_def in attributes.items():
        if not isinstance(element_def, dict):
            continue

        element_info = {
            "type": element_def.get("type", ""),
            "selector": element_def.get("selector", ""),
            "elementType": element_def.get("elementType", element_name),
        }

        # Extract decoration groups (these define what style categories are available).
        settings = element_def.get("settings", {})
        decoration = settings.get("decoration", {})
        element_info["decoration_groups"] = sorted(decoration.keys()) if isinstance(decoration, dict) else []

        # Extract style props (CSS property mappings).
        style_props = element_def.get("styleProps", {})
        element_info["style_props"] = sorted(style_props.keys()) if isinstance(style_props, dict) else []

        # Extract advanced settings.
        advanced = settings.get("advanced", {})
        element_info["advanced_groups"] = sorted(advanced.keys()) if isinstance(advanced, dict) else []

        elements[element_name] = element_info

    return elements


def build_module_reference(module_json: dict, module_defaults: dict) -> dict:
    """
    Build a complete reference entry for a single module, combining schema
    information with default values.
    """
    module_name = module_json.get("name", "unknown")

    ref = {
        "name": module_name,
        "title": module_json.get("title", ""),
        "category": module_json.get("category", ""),
        "elements": extract_settable_paths_from_schema(module_json),
        "defaults": {},
        "default_paths": {},
    }

    # Flatten defaults into dot paths.
    if module_defaults:
        for element_name, element_defaults in module_defaults.items():
            if isinstance(element_defaults, dict):
                flat = flatten_paths(element_defaults, element_name)
                ref["default_paths"].update(flat)
                ref["defaults"][element_name] = element_defaults

    return ref


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Extract Divi 5 module attribute reference from source files.",
    )
    parser.add_argument(
        "--divi-path",
        type=Path,
        default=Path(__file__).parent.parent / "Divi",
        help="Path to the Divi theme directory (default: ../Divi)",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path(__file__).parent / "divi-module-reference.json",
        help="Output path (default: ./divi-module-reference.json)",
    )
    args = parser.parse_args()

    divi_path = args.divi_path
    modules_dir = divi_path / "includes" / "builder-5" / "visual-builder" / "packages" / "module-library" / "src" / "components"
    defaults_file = divi_path / "includes" / "builder-5" / "server" / "_all_modules_default_printed_style_attributes.php"

    if not modules_dir.exists():
        print(f"Error: modules directory not found: {modules_dir}")
        return

    # Parse defaults.
    all_defaults = {}
    if defaults_file.exists():
        print(f"Parsing defaults from {defaults_file.name}...")
        all_defaults = parse_php_defaults(defaults_file)
        print(f"  Found defaults for {len(all_defaults)} modules")
    else:
        print(f"Warning: defaults file not found: {defaults_file}")

    # Process each module.
    reference = {}
    module_dirs = sorted([d for d in modules_dir.iterdir() if d.is_dir()])

    print(f"Processing {len(module_dirs)} module directories...")

    for module_dir in module_dirs:
        module_json_path = module_dir / "module.json"
        if not module_json_path.exists():
            continue

        try:
            module_json = json.loads(module_json_path.read_text())
        except json.JSONDecodeError as e:
            print(f"  Warning: Could not parse {module_json_path}: {e}")
            continue

        module_name = module_json.get("name", f"divi/{module_dir.name}")
        # The defaults file uses the directory name (without divi/ prefix) as key.
        dir_name = module_dir.name
        module_defaults = all_defaults.get(dir_name, {})

        ref = build_module_reference(module_json, module_defaults)
        reference[module_name] = ref

    # Write output.
    args.output.write_text(json.dumps(reference, indent=2))

    # Summary.
    total_modules = len(reference)
    total_elements = sum(len(m["elements"]) for m in reference.values())
    total_default_paths = sum(len(m["default_paths"]) for m in reference.values())
    modules_with_defaults = sum(1 for m in reference.values() if m["defaults"])

    print(f"\nWrote {args.output}")
    print(f"  {total_modules} modules")
    print(f"  {total_elements} elements (settable attribute groups)")
    print(f"  {total_default_paths} default value paths")
    print(f"  {modules_with_defaults} modules with defaults")

    # Print a sample for verification.
    print(f"\n── Sample: divi/text ──")
    if "divi/text" in reference:
        text_ref = reference["divi/text"]
        for elem_name, elem_info in text_ref["elements"].items():
            print(f"  {elem_name}:")
            print(f"    decoration: {', '.join(elem_info['decoration_groups'])}")
            print(f"    style_props: {', '.join(elem_info['style_props'])}")
        if text_ref["default_paths"]:
            print(f"  defaults ({len(text_ref['default_paths'])} paths):")
            for path, value in list(text_ref["default_paths"].items())[:10]:
                print(f"    {path} = {value}")


if __name__ == "__main__":
    main()
