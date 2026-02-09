# ARIA Management Scripts

This directory contains scripts for ARIA environment management and document format conversion.

## Environment Management Scripts

### create-worktree.sh

Creates Git worktrees for isolated ARIA development and testing environments.

**Usage:**
```bash
.moai/scripts/create-worktree.sh [aria-dev|pure-test|all]
```

**Options:**
- `aria-dev` - Create ARIA development worktree only
- `pure-test` - Create pure test worktree only (without ARIA files)
- `all` - Create both worktrees (recommended)

**Example:**
```bash
# Create both worktrees
.moai/scripts/create-worktree.sh all
```

**What it creates:**
- `../agent-skills-aria-dev/` - ARIA development environment with all ARIA files
- `../agent-skills-pure-test/` - Pure test environment without ARIA files

### switch-env.sh

Switches between different ARIA/MoAI-ADK environments.

**Usage:**
```bash
.moai/scripts/switch-env.sh [aria-dev|pure-test|moai-main]
```

**Options:**
- `aria-dev` - Switch to ARIA development environment
- `pure-test` - Switch to pure test environment (no ARIA)
- `moai-main` - Switch to MoAI-ADK main environment

**Example:**
```bash
# Switch to ARIA development environment
.moai/scripts/switch-env.sh aria-dev

# Switch to pure test environment
.moai/scripts/switch-env.sh pure-test

# Switch back to main
.moai/scripts/switch-env.sh moai-main
```

**Output:**
The script displays:
- Environment path
- Current branch
- ARIA files status (present/absent)
- CLAUDE.md type (ARIA/MoAI-ADK)

## Environment Structure

### MoAI-ADK Main Environment (Current)
- **Path:** `~/Project/Agent-Skills/`
- **Branch:** `main`
- **ARIA Files:** No
- **Purpose:** MoAI-ADK core development

### ARIA Development Environment
- **Path:** `~/Project/agent-skills-aria-dev/`
- **Branch:** `aria/feature-env-setup`
- **ARIA Files:** Yes (all ARIA files included)
- **Purpose:** ARIA feature development

### Pure Test Environment
- **Path:** `~/Project/agent-skills-pure-test/`
- **Branch:** `aria/test-pure-env`
- **ARIA Files:** No (ARIA files excluded via .gitignore)
- **Purpose:** Test ARIA's impact on pure MoAI-ADK environment

## Document Conversion Scripts

### convert-output.sh

Main conversion script for transforming documents between formats.

**Features:**
- Markdown to HTML conversion
- Markdown to PDF conversion (via Pandoc or wkhtmltopdf)
- Markdown to Word conversion (via Pandoc)
- HTML to PDF conversion
- Automatic accessibility attribute injection
- Tool availability checking
- Fallback to Markdown if conversion fails

**Usage:**
```bash
./convert-output.sh [OPTIONS] INPUT_FILE OUTPUT_FORMAT [OUTPUT_FILE]
```

**Examples:**
```bash
# Convert Markdown to HTML
./convert-output.sh document.md html

# Convert Markdown to PDF
./convert-output.sh document.md pdf output.pdf

# Convert Markdown to Word
./convert-output.sh document.md word

# Check tool availability
./convert-output.sh --check-tools
```

**Supported Conversions:**
- Markdown → HTML
- Markdown → PDF
- Markdown → Word (.docx)
- HTML → PDF

**Dependencies:**
- Pandoc (optional, for advanced conversions)
- wkhtmltopdf (optional, for PDF generation)
- LaTeX (optional, for PDF generation via Pandoc)

**Exit Codes:**
- 0: Success
- 1: Conversion failed
- 2: Invalid arguments

### validate-accessibility.sh

Accessibility validation script for WCAG 2.1 AA and PDF/UA compliance.

**Features:**
- HTML WCAG 2.1 AA validation
- PDF/UA compliance checking
- Word document accessibility checks
- Automated test suite
- Detailed validation reports

**Usage:**
```bash
./validate-accessibility.sh [OPTIONS] FILE OUTPUT_FORMAT [REPORT_FILE]
```

**Examples:**
```bash
# Validate HTML
./validate-accessibility.sh document.html html

# Validate PDF with custom report
./validate-accessibility.sh document.pdf pdf custom-report.md

# Validate Word in strict mode
./validate-accessibility.sh document.docx word --strict
```

**Validation Checks:**

**HTML (WCAG 2.1 AA):**
- Language attribute presence
- Document title
- Heading structure (H1-H6)
- Alt text for images
- Link descriptiveness
- Table headers with scope
- Form labels
- Skip navigation link
- Color contrast (manual check)
- ARIA attributes

**PDF (PDF/UA):**
- File structure validation
- Tagged PDF checking
- Metadata completeness
- Embedded fonts
- Reading order

**Word:**
- File structure
- Content validation
- Style consistency

**Exit Codes:**
- 0: All checks passed
- 1: Some checks failed (or warnings in strict mode)
- 2: Validation error occurred

## Configuration

Scripts use configuration from `.moai/config/sections/output.yaml`:

```yaml
output:
  default_format: "markdown"
  formats:
    html:
      css_theme: "regulatory-standard"
      accessibility: "wcag-2.1-aa"
    pdf:
      page_size: "letter"
      margins: "0.75in"
      tagged_pdf: true
      accessibility: "pdf-ua"
```

## Directory Structure

```
.moai/scripts/
├── convert-output.sh           # Main conversion script
├── validate-accessibility.sh   # Accessibility validation
└── README.md                   # This file
```

## Tool Availability

The scripts automatically check for available tools:

### Pandoc
- **Purpose:** Advanced document conversion
- **Install:** `brew install pandoc` (macOS) or `apt-get install pandoc` (Linux)
- **Website:** https://pandoc.org/

### wkhtmltopdf
- **Purpose:** HTML to PDF conversion
- **Install:** `brew install wkhtmltopdf` (macOS) or `apt-get install wkhtmltopdf` (Linux)
- **Website:** https://wkhtmltopdf.org/

### Ghostscript
- **Purpose:** PDF manipulation and tagging
- **Install:** `brew install ghostscript` (macOS) or `apt-get install ghostscript` (Linux)
- **Website:** https://www.ghostscript.com/

### PDF Tools
- **pdfinfo:** PDF metadata extraction (part of poppler-utils)
- **pdffonts:** PDF font analysis (part of poppler-utils)
- **Install:** `apt-get install poppler-utils` (Linux) or `brew install poppler` (macOS)

## Error Handling

Scripts implement robust error handling:

1. **Tool Not Available:** Falls back to internal conversion or warns user
2. **Invalid Input:** Clear error messages with usage examples
3. **Conversion Failure:** Detailed error logging with recovery suggestions
4. **Accessibility Issues:** Warnings for manual review

## Logging

Conversion and validation logs are stored in `.moai/logs/`:

- `output-conversion.log` - Conversion operations
- `accessibility-validation.log` - Validation results

## Examples

### Complete Workflow

```bash
# 1. Convert Markdown to HTML
./convert-output.sh regulatory-doc.md html

# 2. Validate HTML accessibility
./validate-accessibility.sh regulatory-doc.html html

# 3. Convert to PDF for submission
./convert-output.sh regulatory-doc.md pdf submission.pdf

# 4. Validate PDF accessibility
./validate-accessibility.sh submission.pdf pdf
```

### Batch Conversion

```bash
# Convert multiple documents
for file in docs/*.md; do
  ./convert-output.sh "$file" html
done

# Validate all HTML files
for file in docs/*.html; do
  ./validate-accessibility.sh "$file" html
done
```

### Custom Styling

```bash
# Use custom CSS theme
./convert-output.sh document.md html --theme company-branding

# Custom Word template
PANDOC_REFERENCE_DOC=/path/to/template.dotx ./convert-output.sh document.md word
```

## Troubleshooting

### Conversion Fails

1. Check tool availability: `./convert-output.sh --check-tools`
2. Verify input file exists and is readable
3. Check logs in `.moai/logs/output-conversion.log`
4. Try fallback to Markdown

### Accessibility Validation Fails

1. Review validation report for specific issues
2. Check WCAG 2.1 AA requirements
3. Validate with online tools (WAVE, axe)
4. Test with screen readers (NVDA, JAWS)

### PDF Generation Issues

1. Verify Pandoc or wkhtmltopdf is installed
2. Check LaTeX installation (for Pandoc PDF)
3. Ensure sufficient disk space
4. Try alternative PDF tool

## Best Practices

1. **Always Validate:** Validate output after conversion
2. **Check Accessibility:** Use automated and manual testing
3. **Test with Screen Readers:** Verify real-world accessibility
4. **Keep Tools Updated:** Maintain current versions of conversion tools
5. **Review Logs:** Check logs for warnings and errors
6. **Backup Originals:** Keep original Markdown documents
7. **Version Control:** Track template and script changes

## Regulatory Compliance

Scripts support regulatory submission requirements:

- **FDA eCopy:** PDF with bookmarks and hyperlinks
- **EU MDR:** Tagged PDF with proper structure
- **MFDS:** Korean language support
- **ISO 13485:** Quality documentation formatting

## Contributing

When adding new features:

1. Update this README
2. Add usage examples
3. Document dependencies
4. Include accessibility considerations
5. Test with various input formats

## License

These scripts are part of the ARIA (AI Regulatory Intelligence Assistant) project.

## Version

Current version: 1.0.0
Last updated: 2026-02-09
