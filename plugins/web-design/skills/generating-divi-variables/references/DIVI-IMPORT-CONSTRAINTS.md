# Divi 5 Import Constraints

Hard requirements discovered through source code analysis. The generator enforces these, but understanding them helps diagnose import failures.

## Colors Go Through `global_colors`, Not `global_variables`

Divi's `import_global_variables()` method only accepts types: `numbers`, `strings`, `images`, `links`, `fonts`. The type `"colors"` is **silently dropped**. All colors — built-in and custom — must be in the `global_colors` tuple array.

The generator includes colors in `global_variables` for builder UI consistency (Divi's own exports include them), but these entries are not used by the import path.

## System Color IDs Are Fixed

The 5 built-in color slots have fixed IDs:

| Slot | ID |
|------|----|
| Primary | `gcid-primary-color` |
| Secondary | `gcid-secondary-color` |
| Heading | `gcid-heading-color` |
| Body | `gcid-body-color` |
| Link | `gcid-link-color` |

These are stored separately in WordPress Customizer options and merged at runtime.

## System Font IDs Are Reserved

`--et_global_heading_font` and `--et_global_body_font` are stored in WordPress options (not `global_variables`) and are skipped during `import_global_variables()`. They're included in the export for the builder UI but saved via a separate code path during import.

## Custom Variable ID Prefixes

- Colors: `gcid-` prefix (hash-based, 10 chars)
- All other types: `gvid-` prefix (hash-based, 10 chars)

The generator produces stable IDs: same namespace + name always produces the same ID. Safe to re-import.

## Variable Reference Syntax

References between variables and in presets use `$variable()` syntax:

```
Color reference:
$variable({"type":"color","value":{"name":"gcid-xxx","settings":{}}})$

Non-color reference (numbers, strings, fonts, links):
$variable({"type":"content","value":{"name":"gvid-xxx","settings":{}}})$
```

Colors use `"type":"color"`. All other variable types use `"type":"content"`.

## Presets Require Both `attrs` and `styleAttrs`

Divi exports both fields with identical content. The generator duplicates attrs into styleAttrs automatically. Missing styleAttrs may cause preset styles to not render.

## Global Colors Use Tuple Format

The `global_colors` array uses tuple format, not objects:

```json
["gcid-xxx", {"color": "#hex", "status": "active", "label": "Name"}]
```

This differs from `global_variables` which uses flat objects.

## Inactive Color Zombie Bug

When colors are "deleted" in the Divi UI, they persist in the database with `"status":"inactive"`. Re-importing the same gcid should overwrite them back to `"active"`, but this may fail if the Visual Builder is open (its save overwrites the import).

If colors appear missing after import:
1. Ensure Visual Builder was closed during import
2. Check for inactive duplicates in the database
3. Consider purging inactive colors via WP CLI or the reset plugin before re-importing
