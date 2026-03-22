#!/usr/bin/env python3
"""
Extract a complete Divi 5 module preset reference.

For each module, combines four source files:
  - module.json                              — element structure, decoration groups, hover flags
  - conversion-outline.json                  — maps properties to styleAttrs vs renderAttrs
  - module-default-printed-style-attributes  — value shapes for decoration.* (styleAttrs)
  - module-default-render-attributes         — value shapes for advanced.*/meta.* (renderAttrs)

Output: tmp/module-reference-v2.json

Usage:
  python3 tmp/extract_module_reference_v2.py
  python3 tmp/extract_module_reference_v2.py --divi-path /path/to/Divi
  python3 tmp/extract_module_reference_v2.py --module button   # single module
"""

import argparse
import json
from pathlib import Path


DIVI_DEFAULT = Path(__file__).parent.parent / ".." / ".." / ".." / "Divi" / "Divi"


# ── Conversion outline analysis ──────────────────────────────────────────────

def _walk_outline(node, path_so_far: list, results: dict):
    """
    Recursively walk a conversion outline node and collect leaf mappings.

    Each leaf value is a string like:
      "module.decoration.spacing"         → styleAttrs  (decoration.*)
      "module.advanced.text"              → renderAttrs (advanced.*)
      "module.meta.adminLabel"            → renderAttrs (meta.*)
      "button.innerContent.*.text"        → renderAttrs (innerContent)
      "button.decoration.button.*.enable" → renderAttrs (decoration.button)
      "button"                            → element self-reference, skip

    We classify by the mapped target path.
    """
    if isinstance(node, str):
        # Skip bare element self-references (e.g. "button" with no dot path).
        if "." in node:
            results[node] = _classify_target(node)
    elif isinstance(node, dict):
        for k, v in node.items():
            if k == "default":
                _walk_outline(v, path_so_far, results)
            else:
                _walk_outline(v, path_so_far + [k], results)
    elif isinstance(node, list):
        for item in node:
            _walk_outline(item, path_so_far, results)


def _classify_target(target: str) -> str:
    """
    Classify a conversion outline target path as 'styleAttrs' or 'renderAttrs'.

    Rules derived from Divi source (Conversion.php):
      - *.decoration.* → styleAttrs  (CSS properties)
      - *.advanced.*   → renderAttrs (HTML/script)
      - *.meta.*       → renderAttrs
      - *.innerContent.* → renderAttrs (content fields)
      - css.*          → styleAttrs

    Special case: *.decoration.button.* — the button decoration group controls
    HTML rendering state (enable flag, icon), not CSS. Routes to renderAttrs
    despite being under decoration.
    """
    parts = target.split(".")
    for i, part in enumerate(parts):
        if part == "decoration":
            # Check if the next part is "button" — that's renderAttrs territory.
            next_part = parts[i + 1] if i + 1 < len(parts) else ""
            if next_part == "button":
                return "renderAttrs"
            return "styleAttrs"
        if part in ("advanced", "meta", "innerContent"):
            return "renderAttrs"
        if part == "css":
            return "styleAttrs"
    return "unknown"


def parse_conversion_outline(path: Path) -> dict:
    """
    Parse a conversion-outline.json and return a dict of:
      {
        "styleAttrs_paths": [...],   # target paths that go to styleAttrs
        "renderAttrs_paths": [...],  # target paths that go to renderAttrs
        "raw": {...}                 # full outline for reference
      }
    """
    if not path.exists():
        return {"styleAttrs_paths": [], "renderAttrs_paths": [], "raw": {}}

    outline = json.loads(path.read_text())
    # Remove comment key
    outline.pop("_comment", None)

    mappings = {}
    for section_key, section in outline.items():
        _walk_outline(section, [section_key], mappings)

    style_paths = sorted(p for p, cls in mappings.items() if cls == "styleAttrs")
    render_paths = sorted(p for p, cls in mappings.items() if cls == "renderAttrs")
    unknown_paths = sorted(p for p, cls in mappings.items() if cls == "unknown")

    return {
        "styleAttrs_paths": style_paths,
        "renderAttrs_paths": render_paths,
        "unknown_paths": unknown_paths,
        "raw": outline,
    }


# ── Module.json analysis ──────────────────────────────────────────────────────

def _extract_hover_disabled_fields(settings: dict, path_prefix: str, results: list):
    """
    Walk a settings subtree looking for fields with features.hover = false.
    Only collects top-level attrName values — skips component prop paths.
    """
    if not isinstance(settings, dict):
        return
    for key, val in settings.items():
        if key == "component":
            # Skip component prop trees — these are UI definition, not preset paths.
            continue
        if isinstance(val, dict):
            item = val.get("item", val)
            if isinstance(item, dict):
                features = item.get("features", {})
                if isinstance(features, dict) and features.get("hover") is False:
                    attr_name = item.get("attrName")
                    if attr_name:
                        results.append(attr_name)
            _extract_hover_disabled_fields(val, f"{path_prefix}.{key}", results)


def parse_module_json(path: Path) -> dict:
    """
    Parse a module.json and return structured element info:
      {
        "name": "divi/button",
        "title": "Button",
        "category": "module",
        "elements": {
          "module": {
            "selector": "...",
            "decoration_groups": [...],
            "advanced_groups": [...],
            "style_props": [...],
            "hover_disabled_fields": [...]
          },
          ...
        }
      }
    """
    if not path.exists():
        return {}

    data = json.loads(path.read_text())
    data.pop("_comment", None)

    result = {
        "name": data.get("name", ""),
        "title": data.get("title", ""),
        "category": data.get("category", ""),
        "elements": {},
    }

    for elem_name, elem_def in data.get("attributes", {}).items():
        if not isinstance(elem_def, dict):
            continue

        settings = elem_def.get("settings", {})
        decoration = settings.get("decoration", {})
        advanced = settings.get("advanced", {})
        style_props = elem_def.get("styleProps", {})

        hover_disabled = []
        _extract_hover_disabled_fields(settings, elem_name, hover_disabled)

        result["elements"][elem_name] = {
            "selector": elem_def.get("selector", ""),
            "elementType": elem_def.get("elementType", elem_name),
            "decoration_groups": sorted(decoration.keys()) if isinstance(decoration, dict) else [],
            "advanced_groups": sorted(advanced.keys()) if isinstance(advanced, dict) else [],
            "style_props": sorted(style_props.keys()) if isinstance(style_props, dict) else [],
            "hover_disabled_fields": sorted(set(hover_disabled)),
        }

    return result


# ── Default attribute files ───────────────────────────────────────────────────

def flatten_paths(obj, prefix="") -> dict:
    """Flatten nested dict to dot-separated paths with leaf values."""
    result = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            new_prefix = f"{prefix}.{key}" if prefix else key
            if isinstance(value, dict):
                result.update(flatten_paths(value, new_prefix))
            else:
                result[new_prefix] = value
    return result


def parse_defaults(path: Path) -> dict:
    """
    Parse a module-default-*-attributes.json file.
    Returns {"tree": {...}, "flat_paths": {...}}
    """
    if not path.exists():
        return {"tree": {}, "flat_paths": {}}

    data = json.loads(path.read_text())
    data.pop("_comment", None)

    return {
        "tree": data,
        "flat_paths": flatten_paths(data),
    }


# ── Value shape extraction ────────────────────────────────────────────────────

def extract_value_shapes(defaults_tree: dict) -> dict:
    """
    From a defaults tree, extract the shape of each decoration group's value.

    E.g. from:
      { "title": { "decoration": { "font": { "font": { "desktop": { "value": {
          "size": "22px", "lineHeight": "1em" } } } } } } }

    Returns:
      { "title.decoration.font": { "size": "22px", "lineHeight": "1em" } }
    """
    shapes = {}

    def walk(node, path):
        if not isinstance(node, dict):
            return
        # If we find a "value" key inside a device key, that's a value shape.
        if "value" in node and isinstance(node["value"], dict):
            shapes[path] = node["value"]
            return
        for key, val in node.items():
            walk(val, f"{path}.{key}" if path else key)

    walk(defaults_tree, "")
    return shapes


# ── Per-module reference builder ──────────────────────────────────────────────

def build_module_reference(module_dir: Path) -> dict:
    """
    Build a complete reference entry for a single module from its four source files.
    """
    module_json_data = parse_module_json(module_dir / "module.json")
    conversion_data = parse_conversion_outline(module_dir / "conversion-outline.json")
    style_defaults = parse_defaults(module_dir / "module-default-printed-style-attributes.json")
    render_defaults = parse_defaults(module_dir / "module-default-render-attributes.json")

    style_value_shapes = extract_value_shapes(style_defaults["tree"])
    render_value_shapes = extract_value_shapes(render_defaults["tree"])

    return {
        "name": module_json_data.get("name", f"divi/{module_dir.name}"),
        "title": module_json_data.get("title", ""),
        "category": module_json_data.get("category", ""),
        "elements": module_json_data.get("elements", {}),
        "conversion": {
            "styleAttrs_paths": conversion_data["styleAttrs_paths"],
            "renderAttrs_paths": conversion_data["renderAttrs_paths"],
            "unknown_paths": conversion_data.get("unknown_paths", []),
        },
        "style_defaults": {
            "tree": style_defaults["tree"],
            "value_shapes": style_value_shapes,
        },
        "render_defaults": {
            "tree": render_defaults["tree"],
            "value_shapes": render_value_shapes,
        },
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Extract complete Divi 5 module preset reference (v2).",
    )
    parser.add_argument(
        "--divi-path",
        type=Path,
        default=DIVI_DEFAULT,
        help="Path to the Divi theme directory.",
    )
    parser.add_argument(
        "--module",
        type=str,
        default=None,
        help="Extract a single module by directory name (e.g. 'button'). Omit for all.",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path(__file__).parent / "module-reference-v2.json",
        help="Output path (default: tmp/module-reference-v2.json).",
    )
    args = parser.parse_args()

    divi_path = args.divi_path.resolve()
    modules_dir = divi_path / "includes" / "builder-5" / "visual-builder" / "packages" / "module-library" / "src" / "components"

    if not modules_dir.exists():
        print(f"Error: modules directory not found: {modules_dir}")
        return

    if args.module:
        module_dirs = [modules_dir / args.module]
        if not module_dirs[0].exists():
            print(f"Error: module directory not found: {module_dirs[0]}")
            return
    else:
        module_dirs = sorted([d for d in modules_dir.iterdir() if d.is_dir()])

    print(f"Processing {len(module_dirs)} module(s)...")

    reference = {}
    for module_dir in module_dirs:
        if not (module_dir / "module.json").exists():
            continue
        ref = build_module_reference(module_dir)
        reference[ref["name"]] = ref
        print(f"  {ref['name']} — {len(ref['elements'])} elements, "
              f"{len(ref['conversion']['styleAttrs_paths'])} style paths, "
              f"{len(ref['conversion']['renderAttrs_paths'])} render paths")

    args.output.write_text(json.dumps(reference, indent=2))

    total_elements = sum(len(m["elements"]) for m in reference.values())
    total_style = sum(len(m["conversion"]["styleAttrs_paths"]) for m in reference.values())
    total_render = sum(len(m["conversion"]["renderAttrs_paths"]) for m in reference.values())

    print(f"\nWrote {args.output}")
    print(f"  {len(reference)} modules")
    print(f"  {total_elements} total elements")
    print(f"  {total_style} total styleAttrs paths")
    print(f"  {total_render} total renderAttrs paths")


if __name__ == "__main__":
    main()
