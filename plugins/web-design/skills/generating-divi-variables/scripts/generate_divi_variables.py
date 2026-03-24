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
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# Path to the design-system.css file shipped with the skill.
# Resolved relative to this script file so it works regardless of cwd.
_SCRIPT_DIR = Path(__file__).parent
_CSS_SOURCE  = _SCRIPT_DIR.parent / "references" / "design-system.css"

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")

# Regex to find all $ref(name) tokens inside a string value.
_REF_PATTERN = re.compile(r'\$ref\(([^)]+)\)')

# ── Modular type scales ───────────────────────────────────────────────────────
# Ordered from smallest to largest ratio. Two steps down from desktop = mobile.

MODULAR_SCALES = [
    ("minor-second",    1.067),
    ("major-second",    1.125),
    ("minor-third",     1.200),
    ("major-third",     1.250),
    ("perfect-fourth",  1.333),
    ("augmented-fourth",1.414),
    ("perfect-fifth",   1.500),
    ("golden-ratio",    1.618),
]

# Lookup by name or by float value (rounded to 3 decimal places).
_SCALE_BY_NAME  = {name: ratio for name, ratio in MODULAR_SCALES}
_SCALE_BY_VALUE = {round(ratio, 3): (name, i) for i, (name, ratio) in enumerate(MODULAR_SCALES)}
_SCALE_ORDER    = [name for name, _ in MODULAR_SCALES]


def resolve_scale(scale_input) -> tuple[str, float, int]:
    """
    Accept a scale name (str) or ratio (float/int).
    Returns (name, ratio, index) or raises ValueError.
    """
    if isinstance(scale_input, str):
        key = scale_input.strip().lower()
        if key not in _SCALE_BY_NAME:
            raise ValueError(
                f"Unknown scale name '{scale_input}'. "
                f"Valid names: {', '.join(_SCALE_ORDER)}"
            )
        ratio = _SCALE_BY_NAME[key]
        idx   = _SCALE_ORDER.index(key)
        return key, ratio, idx
    else:
        rounded = round(float(scale_input), 3)
        if rounded not in _SCALE_BY_VALUE:
            raise ValueError(
                f"Unknown scale ratio {scale_input}. "
                f"Valid ratios: {', '.join(str(r) for _, r in MODULAR_SCALES)}"
            )
        name, idx = _SCALE_BY_VALUE[rounded]
        return name, rounded, idx


def build_type_scale_numbers(spec: dict) -> dict:
    """
    Expand a type_scale section into number variable entries.

    YAML format:
      type_scale:
        scale: "perfect-fourth"   # or 1.333
        base: "1rem"              # default: "1rem"
        steps: 6                  # heading levels h1–h6, default 6
        mobile_steps_down: 2      # how many scale positions down for mobile, default 2
        viewport_min: 375         # px, default 375
        viewport_max: 1200        # px, default 1200
        prefix: "type-d"          # variable name prefix, default "type-d"
        body_prefix: "type"       # prefix for body/sm/caption, default "type"

    Generates:
      type-scale-base:  "1rem"
      type-d-h6 through type-d-h1: clamp(mobile, vw, desktop)
      type-body:   "1rem"
      type-body-lg: derived from base * mobile_ratio
      type-sm:     "0.875rem"
      type-caption: "0.75rem"

    Only type-scale-base and the display stops are generated. Body/sm/caption
    are only added if not already present in the numbers section.
    """
    ts = spec.get("type_scale")
    if not ts:
        return {}

    scale_input     = ts.get("scale", "perfect-fourth")
    base_str        = ts.get("base", "1rem")
    steps           = int(ts.get("steps", 6))
    mobile_down     = int(ts.get("mobile_steps_down", 2))
    vp_min          = int(ts.get("viewport_min", 375))
    vp_max          = int(ts.get("viewport_max", 1200))
    prefix          = ts.get("prefix", "type-d")

    desktop_name, desktop_ratio, desktop_idx = resolve_scale(scale_input)
    mobile_idx   = max(0, desktop_idx - mobile_down)
    _, mobile_ratio = MODULAR_SCALES[mobile_idx]

    # Parse base value — extract numeric part and unit.
    base_match = re.match(r'^([0-9.]+)(rem|px|em)$', base_str.strip())
    if not base_match:
        raise ValueError(f"type_scale.base must be a simple CSS value like '1rem' or '16px', got '{base_str}'")
    base_num  = float(base_match.group(1))
    base_unit = base_match.group(2)

    # Convert base to px for vw calculation (assumes 1rem = 16px browser default).
    BASE_PX = {"rem": 16.0, "px": 1.0, "em": 16.0}
    base_px = base_num * BASE_PX[base_unit]

    def step_value(ratio: float, n: int) -> float:
        """Value at step n above base in the original unit (n=1 → base*ratio, etc.)"""
        return base_num * (ratio ** n)

    def fmt(v: float) -> str:
        return f"{round(v, 3)}{base_unit}"

    # Heading levels: h1 is highest step, h6 is lowest (step 1 above base).
    # h6 = base * ratio^1, h5 = base * ratio^2, ... h1 = base * ratio^steps
    result = {}
    result["type-scale-base"] = base_str

    for level in range(steps, 0, -1):  # level=steps → h1, level=1 → h6
        label = f"h{steps - level + 1}"
        desktop_val = step_value(desktop_ratio, level)
        mobile_val  = step_value(mobile_ratio, level)

        # vw midpoint: hit desktop_val at vp_max.
        # desktop_val_px / vp_max * 100 = vw%
        desktop_px = desktop_val * BASE_PX[base_unit]
        vw_val = (desktop_px / vp_max) * 100

        key = f"{prefix}-{label}"
        result[key] = f"clamp({fmt(mobile_val)}, {round(vw_val, 2)}vw, {fmt(desktop_val)})"

    return result

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


def resolve_number_value(raw_value: str, namespace: str, numbers: dict) -> str:
    """
    Resolve $ref(name) tokens inside a number variable's value.

    $ref(name) expands to var(--gvid-xxx), allowing derived tokens like:
      type-h4: "calc($ref(base-size) * 1.777)"
      section-md: "calc($ref(section-unit) * 3)"

    The Divi UI shows a spurious "Invalid unit" error for calc(var(--gvid-...))
    expressions, but they resolve correctly in the browser and editor preview.
    The UI validator is wrong — ignore it.

    The referenced name must be defined elsewhere in the numbers section.
    Unrecognised names are left as-is so the caller can catch them in validation.
    """
    def replace(match):
        ref_name = match.group(1).strip()
        if ref_name in numbers:
            return f"var(--{make_gvid(namespace, ref_name)})"
        return match.group(0)  # leave unresolved — validation will catch it

    return _REF_PATTERN.sub(replace, raw_value)


def validate_number_refs(namespace: str, numbers: dict) -> list[str]:
    """
    Check that every $ref() inside a number value points to a defined key.
    Returns a list of error messages (empty = valid).
    """
    errors = []
    for name, raw_value in numbers.items():
        if not isinstance(raw_value, str):
            continue
        for match in _REF_PATTERN.finditer(raw_value):
            ref_name = match.group(1).strip()
            if ref_name not in numbers:
                errors.append(f"  numbers.{name}: $ref({ref_name}) — not defined in numbers")
    return errors


def resolve_preset_value(raw_value: str, namespace: str, spec: dict) -> str:
    """
    Resolve a preset attribute value.

    If the value starts with "$var(" it's a shorthand reference to a variable
    defined in the spec. Resolve it to the full $variable() syntax.
    Otherwise return the value as-is.

    Shorthand forms:
      $var(variable-name)       -> var(--gvid-xxx)  (direct CSS custom property)
      $color(color-name)        -> $variable({"type":"color","value":{"name":"gcid-xxx",...}})$

    Note: $var() uses direct CSS var() rather than Divi's $variable() content ref.
    Divi's content ref system is buggy for number variables in preset attrs.
    Colors still use $variable() because they go through Divi's color resolution system.
    """
    if isinstance(raw_value, str) and raw_value.startswith("$var(") and raw_value.endswith(")"):
        var_name = raw_value[5:-1]
        # When a boilerplate is in use, variable IDs are semantic (gvid-{name}).
        # Otherwise fall back to hash-based IDs for backwards compatibility.
        if spec.get("boilerplate"):
            return f"var(--gvid-{var_name})"
        gvid_id = make_gvid(namespace, var_name)
        return f"var(--{gvid_id})"

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

    # Collect valid $var() targets: numbers (including type_scale-generated), strings, links, custom fonts.
    var_names = set()
    var_names.update(build_type_scale_numbers(spec).keys())
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


# ── Boilerplate loading and patching ─────────────────────────────────────────

def load_boilerplate(boilerplate_path: Path) -> dict:
    """
    Load a boilerplate.json file and return its structure.
    Strips _comment and _note keys (documentation-only, not valid JSON for Divi).
    """
    def strip_comments(obj):
        if isinstance(obj, dict):
            return {k: strip_comments(v) for k, v in obj.items()
                    if not k.startswith('_')}
        elif isinstance(obj, list):
            return [strip_comments(i) for i in obj]
        return obj

    with open(boilerplate_path) as f:
        raw = json.load(f)
    return strip_comments(raw)


def patch_boilerplate_colors(boilerplate: dict, system_colors: dict,
                              custom_colors: dict, palette_tokens: list,
                              namespace: str, all_color_names: set) -> list:
    """
    Patch the boilerplate's global_colors with brand values.

    Priority (highest to lowest):
    1. system_colors — patch the 5 fixed Divi slots by ID
    2. custom_colors — patch boilerplate semantic slots by label, or add new ones
    3. palette_tokens — add palette CSS stops (skipped if label already exists)
    """
    # Build a mutable index of boilerplate colors by ID and by label.
    colors = [list(entry) for entry in boilerplate.get("global_colors", [])]
    by_id    = {entry[0]: entry for entry in colors}
    by_label = {entry[1]["label"]: entry for entry in colors}

    def resolve_value(value):
        """Resolve a color value — for semantic slots, returns $variable() ref."""
        if isinstance(value, dict) and "ref" in value:
            ref_name = value["ref"]
            target_gcid = resolve_color_id(namespace, ref_name, all_color_names)
            return color_ref_value(target_gcid)
        return value

    # Build a palette hex lookup for system slot resolution.
    # System color slots go into the WP theme customizer which does not
    # understand CSS variable references — they must be literal hex values.
    palette_hex = {name: hex_val for name, hex_val in palette_tokens}

    def resolve_system_value(value):
        """Resolve a system slot color — must be literal hex, never a var ref.

        If a ref: is given, look up the hex in the palette. If the palette
        doesn't have it, fall through to the plain value. This prevents
        $variable() refs from being written to theme customizer slots.
        """
        if isinstance(value, dict) and "ref" in value:
            ref_name = value["ref"]
            if ref_name in palette_hex:
                return palette_hex[ref_name]
            # ref not in palette — caller may have provided a hex directly
            # under a different key; fall back to resolve_value which at
            # least produces a valid-looking value.
            return resolve_value(value)
        return value

    # 1. System color slots — patch by fixed ID.
    # MUST be hex — these go into the WP theme customizer, not Divi's
    # variable system. $variable() refs are silently ignored there.
    for slot_name, slot_id in SYSTEM_COLOR_SLOTS.items():
        if slot_name in system_colors:
            color_value = resolve_system_value(system_colors[slot_name])
            if slot_id in by_id:
                by_id[slot_id][1]["color"] = color_value
            else:
                entry = [slot_id, {"color": color_value, "status": "active",
                                   "label": SYSTEM_COLOR_LABELS[slot_name]}]
                colors.append(entry)
                by_id[slot_id] = entry

    # 2. Custom colors — patch boilerplate semantic slots by label, or append.
    for name, value in custom_colors.items():
        color_value = resolve_value(value)
        gcid = resolve_color_id(namespace, name, all_color_names)
        if name in by_label:
            # Patch existing boilerplate slot.
            by_label[name][1]["color"] = color_value
            by_label[name][0] = gcid  # update ID if namespace differs
        elif gcid in by_id:
            by_id[gcid][1]["color"] = color_value
        else:
            # New color not in boilerplate — append.
            entry = [gcid, {"color": color_value, "status": "active", "label": name}]
            colors.append(entry)
            by_id[gcid] = entry
            by_label[name] = entry

    # 3. Palette CSS tokens — append only if not already present.
    for name, hex_value in palette_tokens:
        if name in custom_colors or name in by_label:
            continue
        gcid = make_gcid(namespace, name)
        entry = [gcid, {"color": hex_value, "status": "active", "label": name}]
        colors.append(entry)
        by_id[gcid] = entry
        by_label[name] = entry

    return colors


def patch_boilerplate_variables(boilerplate: dict, spec: dict,
                                 namespace: str) -> list:
    """
    Patch the boilerplate's global_variables with brand values.

    Handles:
    - fonts: patches --et_global_heading_font and --et_global_body_font by ID
    - overrides: patches variables by label (e.g. type-scale, space-scale)
    - type_scale: re-computes heading clamp values and patches by label
    - numbers: appends brand-specific number variables (or patches if label matches)
    - strings, links: appended as new variables
    """
    # Build mutable list and index by ID and label.
    variables = [dict(e) for e in boilerplate.get("global_variables", [])]
    by_id    = {e["id"]: e for e in variables if "id" in e}
    by_label = {e["label"]: e for e in variables if "label" in e}

    def patch_or_append(vid, label, value, vtype, order=None):
        """Patch an existing entry by ID or label, or append if new."""
        if vid in by_id:
            by_id[vid]["value"] = value
        elif label in by_label:
            by_label[label]["value"] = value
        else:
            entry = {
                "id": vid, "label": label, "value": value,
                "status": "active", "type": vtype,
            }
            if order is not None:
                entry["order"] = order
            variables.append(entry)
            by_id[vid] = entry
            by_label[label] = entry

    # Fonts.
    fonts_spec = spec.get("fonts", {})
    for slot_name, font_id in SYSTEM_FONT_SLOTS.items():
        if slot_name in fonts_spec:
            patch_or_append(font_id, slot_name.title(), fonts_spec[slot_name], "fonts")

    for name, value in fonts_spec.get("custom", {}).items():
        vid = make_gvid(namespace, f"font-{name}")
        patch_or_append(vid, name, value, "fonts")

    # Overrides — patch boilerplate variables by label.
    for label, value in spec.get("overrides", {}).items():
        if label in by_label:
            by_label[label]["value"] = str(value)
        else:
            print(f"  Warning: override '{label}' not found in boilerplate variables",
                  file=sys.stderr)

    # type_scale — re-compute heading clamp values and patch by label.
    type_scale_numbers = build_type_scale_numbers(spec)
    for name, value in type_scale_numbers.items():
        # type_scale generates labels like "type-d-h1", "type-scale-base", etc.
        if name in by_label:
            by_label[name]["value"] = value
        else:
            vid = make_gvid(namespace, name)
            patch_or_append(vid, name, value, "numbers")

    # numbers — brand-specific additions or overrides.
    numbers_spec = spec.get("numbers", {})
    ref_errors = validate_number_refs(namespace, {**type_scale_numbers, **numbers_spec})
    if ref_errors:
        print("Error: unresolved $ref() in numbers:", file=sys.stderr)
        for err in ref_errors:
            print(err, file=sys.stderr)
        import sys as _sys; _sys.exit(1)

    num_order = max((e.get("order", 0) for e in variables if e.get("type") == "numbers"),
                    default=80)
    for name, value in numbers_spec.items():
        resolved = resolve_number_value(str(value), namespace,
                                        {**type_scale_numbers, **numbers_spec})
        vid = make_gvid(namespace, name)
        num_order += 1
        patch_or_append(vid, name, resolved, "numbers", num_order)

    # Strings.
    str_order = max((e.get("order", 0) for e in variables if e.get("type") == "strings"),
                    default=0)
    for name, value in spec.get("strings", {}).items():
        str_order += 1
        vid = make_gvid(namespace, name)
        patch_or_append(vid, name, str(value), "strings", str_order)

    # Links.
    link_order = max((e.get("order", 0) for e in variables if e.get("type") == "links"),
                     default=0)
    for name, value in spec.get("links", {}).items():
        link_order += 1
        vid = make_gvid(namespace, name)
        patch_or_append(vid, name, str(value), "links", link_order)

    return variables


def patch_boilerplate_presets(boilerplate: dict, spec: dict) -> dict:
    """
    Merge brand presets on top of boilerplate presets.

    Name-collision semantics: if a brand preset has the same name as a
    boilerplate preset for the same module, the brand attrs are sparse-merged
    into the boilerplate preset (brand wins on overlap, boilerplate attrs not
    mentioned by brand are preserved). The boilerplate preset's ID is kept so
    the default pointer remains valid.

    Empty boilerplate placeholder presets (no attrs) that are not touched by a
    brand preset are removed from the output — they carry no wiring and would
    only create confusion in the Divi builder.
    """
    from copy import deepcopy
    result = deepcopy(boilerplate.get("presets", {"module": {}, "group": {}}))
    if not isinstance(result, dict):
        result = {"module": {}, "group": {}}
    result.setdefault("module", {})
    result.setdefault("group", {})

    brand_presets = build_presets(spec)
    if not isinstance(brand_presets, dict):
        # No brand presets — still remove untouched empty placeholders.
        for module_name, module_config in list(result["module"].items()):
            _remove_empty_placeholders(module_config, touched_ids=set())
        return result

    for module_name, brand_config in brand_presets.get("module", {}).items():
        if module_name not in result["module"]:
            result["module"][module_name] = {"default": brand_config["default"],
                                              "items": {}}
        base_config = result["module"][module_name]

        # Build a name→id index for existing boilerplate presets.
        bp_by_name = {p["name"]: pid
                      for pid, p in base_config["items"].items()}

        touched_ids = set()
        new_default_id = None

        for pid, brand_preset in brand_config.get("items", {}).items():
            bp_id = bp_by_name.get(brand_preset["name"])
            if bp_id is not None:
                # Name collision — sparse-merge brand attrs into boilerplate preset.
                bp_preset = base_config["items"][bp_id]
                brand_attrs = brand_preset.get("attrs", {})
                if brand_attrs:
                    merged = deep_merge(bp_preset.get("attrs", {}), brand_attrs)
                    bp_preset["attrs"] = merged
                    bp_preset["styleAttrs"] = merged
                touched_ids.add(bp_id)
                if pid == brand_config.get("default"):
                    new_default_id = bp_id
            else:
                # New preset — add as-is.
                base_config["items"][pid] = brand_preset
                touched_ids.add(pid)
                if pid == brand_config.get("default"):
                    new_default_id = pid

        # If brand marked a default: true preset, update the module default.
        if new_default_id:
            base_config["default"] = new_default_id

        _remove_empty_placeholders(base_config, touched_ids)

    # Also remove untouched empty placeholders from modules the brand didn't touch.
    for module_name, module_config in result["module"].items():
        if module_name not in brand_presets.get("module", {}):
            _remove_empty_placeholders(module_config, touched_ids=set())

    # Drop module entries that ended up with no presets at all.
    result["module"] = {k: v for k, v in result["module"].items() if v.get("items")}

    return result


def _remove_empty_placeholders(module_config: dict, touched_ids: set) -> None:
    """
    Remove presets that have no attrs and were not touched by brand YAML.
    Mutates module_config in place.
    """
    to_remove = [
        pid for pid, preset in module_config["items"].items()
        if pid not in touched_ids and not preset.get("attrs")
    ]
    for pid in to_remove:
        del module_config["items"][pid]
    # If the default was removed, reassign to the first remaining preset if any.
    if module_config.get("default") in [pid for pid in to_remove]:
        remaining = list(module_config["items"])
        module_config["default"] = remaining[0] if remaining else None


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

    If the spec includes a 'boilerplate' key, loads that JSON as the base
    and patches brand values on top. Otherwise builds from scratch.

    Colors go into global_colors (the only path Divi imports them through).
    Fonts, numbers, strings, and links go into global_variables.
    """
    namespace = spec["id_namespace"]

    # ── Boilerplate mode ──────────────────────────────────────────────────────
    boilerplate_path = spec.get("boilerplate")
    if boilerplate_path:
        spec_dir = spec.get("_spec_dir", Path("."))
        bp_path = (spec_dir / boilerplate_path).resolve()
        if not bp_path.exists():
            print(f"Error: boilerplate not found: {bp_path}", file=sys.stderr)
            import sys as _sys; _sys.exit(1)
        boilerplate = load_boilerplate(bp_path)

        # Collect all color names for ref validation.
        all_color_names = set()
        for entry in boilerplate.get("global_colors", []):
            all_color_names.add(entry[1].get("label", ""))
        for name in spec.get("system_colors", {}):
            all_color_names.add(name)
        for name in spec.get("colors", {}):
            all_color_names.add(name)
        palette_tokens = []
        palette_css_path = spec.get("palette_css")
        if palette_css_path:
            css_path = (spec.get("_spec_dir", Path(".")) / palette_css_path).resolve()
            if css_path.exists():
                palette_tokens = parse_palette_css(css_path)
                for name, _ in palette_tokens:
                    all_color_names.add(name)
            else:
                print(f"  Warning: palette_css not found: {css_path}", file=sys.stderr)

        # Inject boilerplate variable labels into spec so validate_preset_refs
        # treats them as valid $var() targets.
        bp_var_labels = {e["label"] for e in boilerplate.get("global_variables", [])
                         if "label" in e and e.get("type") != "colors"}
        bp_type_scale = build_type_scale_numbers(spec)
        bp_numbers = spec.get("numbers", {})
        # Merge boilerplate labels + generated type scale + spec numbers into a
        # temporary numbers dict so validation sees all valid targets.
        spec.setdefault("_boilerplate_var_labels", bp_var_labels)
        _orig_numbers = spec.get("numbers", {})
        spec["numbers"] = {**{k: "" for k in bp_var_labels}, **bp_type_scale, **_orig_numbers}

        # Validate preset refs against boilerplate + brand color names.
        ref_errors = validate_preset_refs(spec, all_color_names)
        spec["numbers"] = _orig_numbers  # restore
        if ref_errors:
            print("Error: unresolved preset references:", file=sys.stderr)
            for err in ref_errors:
                print(err, file=sys.stderr)
            import sys as _sys; _sys.exit(1)

        global_colors   = patch_boilerplate_colors(boilerplate,
                              spec.get("system_colors", {}),
                              spec.get("colors", {}),
                              palette_tokens, namespace, all_color_names)
        global_variables = patch_boilerplate_variables(boilerplate, spec, namespace)
        presets          = patch_boilerplate_presets(boilerplate, spec)

        # Strip variables that have moved to design-system.css.
        # These are derived calc chains — they live in :root CSS now and
        # do not belong in the Divi variable UI.
        _css_owned = {
            "type-d-h1", "type-d-h2", "type-d-h3",
            "type-d-h4", "type-d-h5", "type-d-h6",
            "type-body-lg", "type-body", "type-sm", "type-caption",
            "space-xs", "space-sm", "space-md",
            "space-lg", "space-xl", "space-2xl",
            "container-padding",
        }
        global_variables = [
            e for e in global_variables
            if e.get("label") not in _css_owned
        ]

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

    # ── From-scratch mode (no boilerplate) ───────────────────────────────────
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

    # Numbers — merge type_scale-generated tokens first, then explicit numbers.
    # Explicit numbers take precedence (allow overriding generated stops).
    type_scale_numbers = build_type_scale_numbers(spec)
    numbers_spec = {**type_scale_numbers, **spec.get("numbers", {})}
    ref_errors = validate_number_refs(namespace, numbers_spec)
    if ref_errors:
        print("Error: unresolved $ref() in numbers:", file=sys.stderr)
        for err in ref_errors:
            print(err, file=sys.stderr)
        sys.exit(1)

    num_order = 0
    for name, value in numbers_spec.items():
        num_order += 1
        resolved = resolve_number_value(str(value), namespace, numbers_spec)
        global_variables.append({
            "id": make_gvid(namespace, name),
            "label": name,
            "value": resolved,
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

        # Copy design-system.css alongside the JSON output.
        css_out = out_path.with_name("design-system.css")
        if _CSS_SOURCE.exists():
            if _CSS_SOURCE.resolve() != css_out.resolve():
                shutil.copy2(_CSS_SOURCE, css_out)
            # else: output is in the same dir as source — no copy needed
        else:
            print(f"  Warning: design-system.css not found at {_CSS_SOURCE}", file=sys.stderr)

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
        print(f"  → {css_out}")
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
