#!/usr/bin/env python3
"""
Generate Divi 5 global variables and presets JSON from a YAML design spec.

Reads a YAML spec file defining colors, fonts, numbers, strings, links,
and module presets, then produces a Divi-compatible JSON import file.

Colors are imported through global_colors (tuple format); all other variable
types go through global_variables. Presets go through the presets object.
This matches Divi's import path where "colors" is not a valid type for
global_variables — only: numbers, strings, images, links, fonts

Usage:
  python3 generate_divi_variables.py spec-mg.yaml
  python3 generate_divi_variables.py spec-mg.yaml spec-lp.yaml
  python3 generate_divi_variables.py spec-mg.yaml -o output/divi-mg.json
"""

import argparse
import json
import re
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

# Divi's 5 built-in system color slot IDs.
SYSTEM_COLOR_SLOTS = {
    "primary":   "gcid-primary-color",
    "secondary": "gcid-secondary-color",
    "heading":   "gcid-heading-color",
    "body":      "gcid-body-color",
    "link":      "gcid-link-color",
}

# Divi's 2 built-in system font IDs (stored in WP options, not global_variables).
SYSTEM_FONT_SLOTS = {
    "heading": "--et_global_heading_font",
    "body":    "--et_global_body_font",
}

# Labels Divi uses for the built-in system color slots.
SYSTEM_COLOR_LABELS = {
    "primary":   "Primary Color",
    "secondary": "Secondary Color",
    "heading":   "Heading Text Color",
    "body":      "Body Text Color",
    "link":      "Link Color",
}


# ── Stable ID generation ─────────────────────────────────────────────────────
# MD5 of a namespaced key so the same token always gets the same Divi ID.
# Re-running the script produces identical output — safe to import repeatedly
# without creating duplicate variables.

def _stable_hash(namespace: str, kind: str, name: str) -> str:
    return hashlib.md5(f"{namespace}-{kind}:{name}".encode()).hexdigest()[:10]

def make_gcid(namespace: str, name: str) -> str:
    """Stable gcid-* for a color variable."""
    return f"gcid-{_stable_hash(namespace, 'color', name)}"

def make_gvid(namespace: str, name: str) -> str:
    """Stable gvid-* for a non-color variable."""
    return f"gvid-{_stable_hash(namespace, 'var', name)}"


# ── Color reference wrapper ──────────────────────────────────────────────────
# Divi's $variable() syntax for color-to-color references.

def color_ref_value(target_gcid: str) -> str:
    """Wrap a gcid in Divi's $variable() reference syntax."""
    inner = json.dumps({
        "type": "color",
        "value": {"name": target_gcid, "settings": {}},
    }, separators=(",", ":"))
    return f"$variable({inner})$"


# ── Variable reference wrapper (generic) ─────────────────────────────────────
# Divi's $variable() syntax for referencing variables in preset attributes.
# Non-color variables use "type":"content" in presets.

def variable_ref(target_id: str, ref_type: str = "content") -> str:
    """Wrap a variable ID in Divi's $variable() reference syntax."""
    inner = json.dumps({
        "type": ref_type,
        "value": {"name": target_id, "settings": {}},
    }, separators=(",", ":"))
    return f"$variable({inner})$"


# ── Dot-path expansion ───────────────────────────────────────────────────────

def expand_dot_path(path: str, value) -> dict:
    """
    Expand a dot-separated path into a nested dict.
    Example: "a.b.c" with value "x" -> {"a": {"b": {"c": "x"}}}
    """
    parts = path.split(".")
    result = {}
    current = result
    for part in parts[:-1]:
        current[part] = {}
        current = current[part]
    current[parts[-1]] = value
    return result


def deep_merge(base: dict, overlay: dict) -> dict:
    """Recursively merge overlay into base, returning a new dict."""
    result = dict(base)
    for key, value in overlay.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


# ── Preset building ──────────────────────────────────────────────────────────

def _stable_preset_id(namespace: str, module_name: str, preset_name: str) -> str:
    """Stable 10-char alphanumeric ID for a preset."""
    h = hashlib.md5(f"{namespace}-preset:{module_name}:{preset_name}".encode()).hexdigest()[:10]
    return h


def resolve_preset_value(raw_value: str, namespace: str, spec: dict) -> str:
    """
    Resolve a preset attribute value.

    If the value starts with "$var(" it's a shorthand reference to a variable
    defined in the spec. Resolve it to the full $variable() syntax.
    Otherwise return the value as-is.

    Shorthand forms:
      $var(variable-name)       -> $variable({"type":"content","value":{"name":"gvid-xxx",...}})$
      $color(color-name)        -> $variable({"type":"color","value":{"name":"gcid-xxx",...}})$
    """
    if isinstance(raw_value, str) and raw_value.startswith("$var(") and raw_value.endswith(")"):
        var_name = raw_value[5:-1]
        gvid = make_gvid(namespace, var_name)
        return variable_ref(gvid, "content")

    if isinstance(raw_value, str) and raw_value.startswith("$color(") and raw_value.endswith(")"):
        color_name = raw_value[7:-1]
        if color_name in SYSTEM_COLOR_SLOTS:
            gcid = SYSTEM_COLOR_SLOTS[color_name]
        else:
            gcid = make_gcid(namespace, color_name)
        return variable_ref(gcid, "color")

    return raw_value


def validate_preset_refs(spec: dict, all_color_names: set) -> list[str]:
    """
    Validate that all $var() and $color() references in presets point to
    defined variables. Returns a list of error messages (empty = valid).
    """
    errors = []
    presets_spec = spec.get("presets", {})
    if not presets_spec:
        return errors

    # Collect valid $var() targets: numbers, strings, links, custom fonts.
    var_names = set()
    for section in ("numbers", "strings", "links"):
        var_names.update(spec.get(section, {}).keys())
    for name in spec.get("fonts", {}).get("custom", {}).keys():
        var_names.add(f"font-{name}")

    for module_name, preset_def in presets_spec.items():
        if isinstance(preset_def, dict) and "name" in preset_def:
            preset_list = [preset_def]
        elif isinstance(preset_def, list):
            preset_list = preset_def
        else:
            continue

        for preset in preset_list:
            preset_name = preset.get("name", module_name)
            for dot_path, raw_value in preset.get("attrs", {}).items():
                if isinstance(raw_value, str) and raw_value.startswith("$var(") and raw_value.endswith(")"):
                    ref = raw_value[5:-1]
                    if ref not in var_names:
                        errors.append(f"  {module_name} ({preset_name}): $var({ref}) — not defined in numbers/strings/links/fonts.custom")
                elif isinstance(raw_value, str) and raw_value.startswith("$color(") and raw_value.endswith(")"):
                    ref = raw_value[7:-1]
                    if ref not in all_color_names:
                        errors.append(f"  {module_name} ({preset_name}): $color({ref}) — not defined in system_colors/colors/palette_css")

    return errors


def build_presets(spec: dict) -> dict:
    """
    Build the presets object from the spec's presets section.

    YAML format:
      presets:
        divi/text:
          name: "Brand Text"
          default: true          # optional, marks this as the default preset
          attrs:
            content.decoration.bodyFont.body.font.desktop.value.size: "$var(type-body)"
            content.decoration.headingFont.h1.font.desktop.value.size: "$var(type-d-xl)"

    Returns the presets dict in Divi's import format.
    """
    presets_spec = spec.get("presets", {})
    if not presets_spec:
        return []

    namespace = spec["id_namespace"]
    now_ms = int(datetime.now(timezone.utc).timestamp() * 1000)

    module_presets = {}

    for module_name, preset_def in presets_spec.items():
        # Support single preset (dict with name/attrs) or list of presets.
        if isinstance(preset_def, dict) and "name" in preset_def:
            preset_list = [preset_def]
        elif isinstance(preset_def, list):
            preset_list = preset_def
        else:
            continue

        items = {}
        default_id = None

        for preset in preset_list:
            preset_name = preset.get("name", f"{module_name} Preset")
            preset_id = _stable_preset_id(namespace, module_name, preset_name)
            is_default = preset.get("default", False)

            if is_default or default_id is None:
                default_id = preset_id

            # Build attrs by expanding dot paths and resolving variable references.
            attrs = {}
            for dot_path, raw_value in preset.get("attrs", {}).items():
                resolved = resolve_preset_value(raw_value, namespace, spec)
                expanded = expand_dot_path(dot_path, resolved)
                attrs = deep_merge(attrs, expanded)

            item = {
                "id": preset_id,
                "name": preset_name,
                "moduleName": module_name,
                "version": "5.0.0",
                "type": "module",
                "created": now_ms,
                "updated": now_ms,
            }

            if attrs:
                item["attrs"] = attrs
                # Divi exports both attrs and styleAttrs with identical content.
                item["styleAttrs"] = attrs

            items[preset_id] = item

        module_presets[module_name] = {
            "default": default_id,
            "items": items,
        }

    if not module_presets:
        return []

    return {"module": module_presets}


# ── Palette CSS parsing ──────────────────────────────────────────────────────

def parse_palette_css(css_path: Path) -> list[tuple[str, str]]:
    """
    Return ordered list of (token_name, hex_value) from CSS custom properties.
    Preserves source order. Skips duplicate names (first occurrence wins).
    """
    text = css_path.read_text()
    pattern = r'--([a-zA-Z0-9-]+)\s*:\s*(#[0-9A-Fa-f]{3,8})'
    seen = set()
    tokens = []
    for name, value in re.findall(pattern, text):
        if name not in seen:
            seen.add(name)
            tokens.append((name, value.lower()))
    return tokens


# ── Spec parsing ─────────────────────────────────────────────────────────────

def load_spec(spec_path: Path) -> dict:
    """Load and validate a YAML design spec."""
    with open(spec_path) as f:
        spec = yaml.safe_load(f)

    if not isinstance(spec, dict):
        raise ValueError(f"Spec must be a YAML mapping, got {type(spec).__name__}")

    if "name" not in spec:
        raise ValueError("Spec must include a 'name' field")

    # Default namespace to a slug of the name if not provided.
    if "id_namespace" not in spec:
        spec["id_namespace"] = re.sub(r'[^a-z0-9]+', '-', spec["name"].lower()).strip('-')

    return spec


def resolve_color_id(namespace: str, name: str, all_color_names: set) -> str:
    """
    Get the gcid for a color name.

    System color slot names ('primary', 'secondary', etc.) map to their
    fixed Divi IDs. Everything else gets a stable hash-based ID.
    """
    if name in SYSTEM_COLOR_SLOTS:
        return SYSTEM_COLOR_SLOTS[name]
    return make_gcid(namespace, name)


# ── JSON assembly ────────────────────────────────────────────────────────────

def build_divi_json(spec: dict) -> dict:
    """
    Assemble a complete Divi global variables export from a parsed spec.

    Colors go into global_colors (the only path Divi imports them through).
    Fonts, numbers, strings, and links go into global_variables.
    """
    namespace = spec["id_namespace"]

    # Collect all color names so refs can be validated.
    all_color_names = set()

    # System colors.
    system_colors = spec.get("system_colors", {})
    for slot_name in system_colors:
        all_color_names.add(slot_name)

    # Custom colors (from spec).
    custom_colors = spec.get("colors", {})
    for name in custom_colors:
        all_color_names.add(name)

    # Palette CSS colors (optional).
    palette_tokens = []
    palette_css_path = spec.get("palette_css")
    if palette_css_path:
        spec_dir = spec.get("_spec_dir", Path("."))
        css_path = (spec_dir / palette_css_path).resolve()
        if css_path.exists():
            palette_tokens = parse_palette_css(css_path)
            for name, _ in palette_tokens:
                all_color_names.add(name)
        else:
            print(f"  Warning: palette_css not found: {css_path}", file=sys.stderr)

    # ── Build global_colors (tuple format for import) ────────────────────────
    global_colors = []
    color_order = 0

    # 1. System color slots.
    for slot_name, slot_id in SYSTEM_COLOR_SLOTS.items():
        if slot_name in system_colors:
            color_order += 1
            sys_value = system_colors[slot_name]
            if isinstance(sys_value, dict) and "ref" in sys_value:
                ref_name = sys_value["ref"]
                target_gcid = resolve_color_id(namespace, ref_name, all_color_names)
                color_value = color_ref_value(target_gcid)
            else:
                color_value = sys_value
            global_colors.append([
                slot_id,
                {
                    "color": color_value,
                    "status": "active",
                    "label": SYSTEM_COLOR_LABELS[slot_name],
                },
            ])

    # 2. Custom colors from spec.
    for name, value in custom_colors.items():
        color_order += 1
        gcid = resolve_color_id(namespace, name, all_color_names)

        if isinstance(value, dict) and "ref" in value:
            # Reference to another color.
            ref_name = value["ref"]
            target_gcid = resolve_color_id(namespace, ref_name, all_color_names)
            color_value = color_ref_value(target_gcid)
        else:
            color_value = value

        global_colors.append([gcid, {"color": color_value, "status": "active", "label": name}])

    # 3. Palette CSS colors.
    for name, hex_value in palette_tokens:
        # Skip if already defined in custom colors (spec takes precedence).
        if name in custom_colors:
            continue
        color_order += 1
        gcid = make_gcid(namespace, name)
        global_colors.append([gcid, {"color": hex_value, "status": "active", "label": name}])

    # ── Build global_variables (non-color types) ─────────────────────────────
    global_variables = []

    # Colors in global_variables — included for builder UI consistency (Divi's
    # own exports include them) but these are NOT used by the import path.
    gv_color_order = 0
    for slot_name, slot_id in SYSTEM_COLOR_SLOTS.items():
        if slot_name in system_colors:
            gv_color_order += 1
            sys_value = system_colors[slot_name]
            if isinstance(sys_value, dict) and "ref" in sys_value:
                ref_name = sys_value["ref"]
                target_gcid = resolve_color_id(namespace, ref_name, all_color_names)
                gv_color_value = color_ref_value(target_gcid)
            else:
                gv_color_value = sys_value
            global_variables.append({
                "id": slot_id,
                "label": SYSTEM_COLOR_LABELS[slot_name],
                "value": gv_color_value,
                "groupKey": "colors",
                "status": "active",
                "order": gv_color_order,
                "lastUpdated": TIMESTAMP,
                "type": "colors",
            })

    for name, value in custom_colors.items():
        gv_color_order += 1
        gcid = resolve_color_id(namespace, name, all_color_names)
        if isinstance(value, dict) and "ref" in value:
            ref_name = value["ref"]
            target_gcid = resolve_color_id(namespace, ref_name, all_color_names)
            resolved_value = color_ref_value(target_gcid)
        else:
            resolved_value = value
        global_variables.append({
            "id": gcid,
            "label": name,
            "value": resolved_value,
            "status": "active",
            "order": gv_color_order,
            "lastUpdated": TIMESTAMP,
            "variableType": "colors",
            "type": "colors",
        })

    for name, hex_value in palette_tokens:
        if name in custom_colors:
            continue
        gv_color_order += 1
        gcid = make_gcid(namespace, name)
        global_variables.append({
            "id": gcid,
            "label": name,
            "value": hex_value,
            "status": "active",
            "order": gv_color_order,
            "lastUpdated": TIMESTAMP,
            "variableType": "colors",
            "type": "colors",
        })

    # Fonts — system slots + custom.
    fonts_spec = spec.get("fonts", {})
    font_order = 0

    for slot_name, font_id in SYSTEM_FONT_SLOTS.items():
        if slot_name in fonts_spec:
            font_order += 1
            global_variables.append({
                "id": font_id,
                "label": slot_name.title(),
                "value": fonts_spec[slot_name],
                "groupKey": "fonts",
                "status": "active",
                "order": font_order,
                "lastUpdated": TIMESTAMP,
                "type": "fonts",
            })

    for name, value in fonts_spec.get("custom", {}).items():
        font_order += 1
        global_variables.append({
            "id": make_gvid(namespace, f"font-{name}"),
            "label": name,
            "value": value,
            "status": "active",
            "order": font_order,
            "lastUpdated": TIMESTAMP,
            "variableType": "fonts",
            "type": "fonts",
        })

    # Numbers.
    num_order = 0
    for name, value in spec.get("numbers", {}).items():
        num_order += 1
        global_variables.append({
            "id": make_gvid(namespace, name),
            "label": name,
            "value": str(value),
            "status": "active",
            "order": num_order,
            "lastUpdated": TIMESTAMP,
            "variableType": "numbers",
            "type": "numbers",
        })

    # Strings.
    str_order = 0
    for name, value in spec.get("strings", {}).items():
        str_order += 1
        global_variables.append({
            "id": make_gvid(namespace, name),
            "label": name,
            "value": str(value),
            "status": "active",
            "order": str_order,
            "lastUpdated": TIMESTAMP,
            "variableType": "strings",
            "type": "strings",
        })

    # Links.
    link_order = 0
    for name, value in spec.get("links", {}).items():
        link_order += 1
        global_variables.append({
            "id": make_gvid(namespace, name),
            "label": name,
            "value": str(value),
            "status": "active",
            "order": link_order,
            "lastUpdated": TIMESTAMP,
            "variableType": "links",
            "type": "links",
        })

    # ── Validate preset references ────────────────────────────────────────
    ref_errors = validate_preset_refs(spec, all_color_names)
    if ref_errors:
        print("Error: unresolved preset references:", file=sys.stderr)
        for err in ref_errors:
            print(err, file=sys.stderr)
        sys.exit(1)

    # ── Build presets ───────────────────────────────────────────────────────
    presets = build_presets(spec)

    return {
        "context": "et_builder",
        "data": [],
        "presets": presets,
        "global_colors": global_colors,
        "global_variables": global_variables,
        "page_settings_meta": None,
        "canvases": [],
        "images": [],
        "thumbnails": [],
    }


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate Divi 5 global variables JSON from a YAML design spec.",
    )
    parser.add_argument(
        "specs",
        nargs="+",
        type=Path,
        help="One or more YAML spec files to process.",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Output path (only valid with a single spec). Defaults to <spec-stem>.json.",
    )
    args = parser.parse_args()

    if args.output and len(args.specs) > 1:
        parser.error("-o/--output can only be used with a single spec file")

    for spec_path in args.specs:
        if not spec_path.exists():
            print(f"Error: spec not found: {spec_path}", file=sys.stderr)
            sys.exit(1)

        spec = load_spec(spec_path)
        spec["_spec_dir"] = spec_path.parent

        data = build_divi_json(spec)

        if args.output:
            out_path = args.output
        else:
            out_path = spec_path.with_suffix(".json")

        out_path.write_text(json.dumps(data, indent=4))

        # Summary.
        n_gc = len(data["global_colors"])
        gv = data["global_variables"]
        n_fonts = sum(1 for v in gv if v["type"] == "fonts")
        n_nums = sum(1 for v in gv if v["type"] == "numbers")
        n_strs = sum(1 for v in gv if v["type"] == "strings")
        n_links = sum(1 for v in gv if v["type"] == "links")

        n_presets = 0
        if isinstance(data["presets"], dict):
            for mod_presets in data["presets"].get("module", {}).values():
                n_presets += len(mod_presets.get("items", {}))

        print(f"{spec['name']}")
        print(f"  → {out_path}")
        parts = [f"{n_gc} colors", f"{n_fonts} fonts", f"{n_nums} numbers"]
        if n_strs:
            parts.append(f"{n_strs} strings")
        if n_links:
            parts.append(f"{n_links} links")
        if n_presets:
            parts.append(f"{n_presets} presets")
        print(f"    {', '.join(parts)}")
        print()


if __name__ == "__main__":
    main()
