# Technical Context

WordPress is the CMS. ACF Pro handles custom fields. Everything else is determined during Phase 1.

## Determined During Phase 1

- **Page Builder:** (Divi, Elementor, Beaver Builder, Gutenberg blocks, none)
- **Forms Plugin:** (WS Form, Gravity Forms, WPForms, Ninja Forms, Contact Form 7)
- **E-commerce:** (WooCommerce, Easy Digital Downloads, GiveWP for donations, none)
- **Other Integrations:** (CRM, email marketing, analytics, membership plugins)

## Content Generation Implications

- Content files are markdown, not page builder shortcodes — builder-agnostic
- Form specs define behavior (fields, validation, submission), not plugin-specific implementation
- CPTs are registered via code or ACF — `acf-export.json` can be imported directly
- Product/donation pages follow standard content format with additional commerce fields if applicable
