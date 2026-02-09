# ARIA Output Templates

This directory contains company branding templates and styling for ARIA regulatory document output in various formats.

## Directory Structure

```
.moai/templates/
├── css/                    # Stylesheets for HTML output
│   ├── regulatory-standard.css    # Main CSS theme (WCAG 2.1 AA compliant)
│   └── print.css                   # Print-specific styles for PDF generation
├── word/                   # Microsoft Word templates
│   └── regulatory-template.dotx   # Word document template (TODO)
├── pdf/                    # PDF generation templates
│   ├── header.html                 # PDF header template
│   ├── footer.html                 # PDF footer template
│   └── cover.html                  # Cover page template (TODO)
├── html/                   # HTML document templates
│   ├── base.html                   # Base HTML template
│   └── document.html               # Document-specific template (TODO)
└── images/                 # Company branding images
    ├── logo.png                    # Company logo (TODO)
    └── favicon.ico                 # Website favicon (TODO)
```

## CSS Themes

### regulatory-standard.css

Main CSS theme for HTML output with the following features:

- **WCAG 2.1 AA Compliance**: All color contrast ratios meet or exceed 4.5:1 for normal text
- **Semantic HTML**: Uses proper HTML5 semantic elements
- **Responsive Design**: Mobile-friendly layout with breakpoints
- **Print Optimization**: Print-specific styles for PDF generation
- **Accessibility**: Screen reader support, keyboard navigation, ARIA attributes
- **Company Branding**: Customizable colors, fonts, and logos

### CSS Variables

Customize the theme by modifying CSS variables:

```css
:root {
  --color-primary: #0066cc;
  --color-primary-dark: #004499;
  --color-accent: #ff6600;
  --color-text: #333333;
  --color-background: #ffffff;
  --font-family-base: Arial, sans-serif;
  --font-family-heading: Georgia, serif;
}
```

## HTML Templates

### base.html

Base HTML template with the following features:

- Semantic HTML5 structure
- ARIA attributes for accessibility
- Skip navigation link
- Responsive viewport meta tag
- Company branding placeholder
- Footer with copyright and confidentiality notice

### Template Variables

The following variables are available in HTML templates:

- `{{TITLE}}` - Document title
- `{{CSS_PATH}}` - Path to CSS files
- `{{LOGO_PATH}}` - Path to company logo
- `{{FAVICON_PATH}}` - Path to favicon
- `{{CONTENT}}` - Main document content
- `{{YEAR}}` - Current year
- `{{DATE}}` - Document date
- `{{VERSION}}` - ARIA version

## PDF Templates

### header.html

PDF header template with:

- Company logo
- Document title
- Confidentiality notice
- Page numbers (added by PDF generator)

### footer.html

PDF footer template with:

- Document confidentiality notice
- Document title
- Page numbers

## Word Templates

### regulatory-template.dotx

Microsoft Word template (to be created) with:

- Company styles and formatting
- Table styles for regulatory data
- Header and footer
- Page layout settings
- Font and typography settings

## Customization

### Company Branding

To customize for your company:

1. Update CSS variables in `regulatory-standard.css`
2. Add company logo to `images/logo.png`
3. Add favicon to `images/favicon.ico`
4. Update company name in templates
5. Create custom Word template

### Color Scheme

The default color scheme is optimized for regulatory documents:

- Primary: #0066cc (professional blue)
- Secondary: #004499 (dark blue)
- Accent: #ff6600 (orange for warnings)
- Text: #333333 (dark gray for readability)
- Background: #ffffff (white)

### Typography

Default font settings:

- Base: Arial, Helvetica, sans-serif
- Headings: Georgia, serif
- Monospace: Courier New, monospace
- Base size: 16px (HTML), 12pt (PDF/Word)

## Accessibility

All templates are designed for accessibility:

- WCAG 2.1 AA compliance for HTML
- PDF/UA compliance for PDF
- Semantic HTML structure
- ARIA labels and roles
- Keyboard navigation support
- Screen reader compatibility

## Print Styles

Print-specific styles in `print.css`:

- Optimized for 8.5" x 11" paper
- 0.75" margins
- Page breaks before major headings
- Tables avoid page breaks
- Images sized appropriately
- Links show URLs in print

## Regulatory Compliance

Templates support:

- FDA eCopy requirements (PDF format)
- EU MDR documentation standards
- MFDS format requirements
- ISO 13485 quality management documentation

## Usage

### HTML Generation

```bash
# Using the conversion script
.moai/scripts/convert-output.sh document.md html
```

### PDF Generation

```bash
# Convert to PDF with company branding
.moai/scripts/convert-output.sh document.md pdf
```

### Word Generation

```bash
# Convert to Word format
.moai/scripts/convert-output.sh document.md word
```

## Validation

Validate output for accessibility compliance:

```bash
# Validate HTML
.moai/scripts/validate-accessibility.sh document.html html

# Validate PDF
.moai/scripts/validate-accessibility.sh document.pdf pdf

# Validate Word
.moai/scripts/validate-accessibility.sh document.docx word
```

## Notes

- Templates are designed for regulatory document submission
- All styles are inline or embedded to ensure portability
- External dependencies are minimized
- Print styles are optimized for professional output
- Accessibility is prioritized throughout

## Version

Current version: 1.0.0
Last updated: 2026-02-09
