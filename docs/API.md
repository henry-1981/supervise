# Cowork Supervisor API Documentation

## Version 1.1.0

This document describes the API and configuration options for Cowork Supervisor v1.1.0.

---

## Slash Command API

### /supervise

Main entry point for multi-plugin coordination.

#### Syntax

```bash
/supervise "[task description]" [options]
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| task_description | string | Yes | Natural language description of the task |
| --style | string | No | Output style: `moai`, `r2d2`, `yoda` (default: `moai`) |
| --format | string | No | Output format: `markdown`, `html`, `pdf`, `word` (default: `markdown`) |
| --output | string | No | Output file path (for format conversion) |
| --template | string | No | Template to use for PDF/Word generation |

#### Examples

```bash
# Basic usage
/supervise "Analyze competitor financials"

# With output style
/supervise "Review code security" --style r2d2

# With format conversion
/supervise "Generate market report" --format pdf --output report.pdf

# Combined options
/supervise "Prepare executive summary" \
  --style moai \
  --format pdf \
  --output summary.pdf \
  --template executive-template
```

---

## Configuration API

### Output Configuration

Location: `.moai/config/sections/output.yaml`

#### Structure

```yaml
output:
  # Default settings
  default_format: string      # markdown, html, pdf, word
  default_style: string       # moai, r2d2, yoda

  # Format-specific settings
  formats:
    markdown:
      extension: string       # .md
      encoding: string        # utf-8
      line_width: integer     # 80

    html:
      extension: string       # .html
      css_theme: string       # regulatory-standard
      accessibility: string   # wcag-2.1-aa
      include_toc: boolean    # true
      syntax_highlighting: boolean  # true

    pdf:
      extension: string       # .pdf
      page_size: string       # letter, a4
      margins: string         # 0.75in
      toc: boolean           # true
      bookmarks: boolean     # true
      metadata:
        author: string
        subject: string
        keywords: array

    word:
      extension: string       # .docx
      template: string       # regulatory-template.dotx
      track_changes: boolean  # false

  # Style-specific settings
  styles:
    moai:
      language_aware: boolean      # true
      show_progress: boolean       # true
      bilingual_support: boolean   # true
      emoji_decorations: boolean   # true

    r2d2:
      concise: boolean            # true
      technical: boolean          # true
      code_focused: boolean       # true
      minimal_formatting: boolean # true

    yoda:
      wisdom_focused: boolean     # true
      strategic: boolean          # true
      thoughtful: boolean         # true
      educational: boolean        # true
```

#### Example Configuration

```yaml
output:
  default_format: html
  default_style: moai

  formats:
    html:
      css_theme: "company-branding"
      accessibility: "wcag-2.1-aa"
      include_toc: true

    pdf:
      page_size: "a4"
      margins: "1in"
      metadata:
        author: "Company Name"
        subject: "Regulatory Submission"

  styles:
    moai:
      show_progress: true
      emoji_decorations: true
```

---

## Script API

### convert-output.sh

Convert output files between formats.

#### Syntax

```bash
.moai/scripts/convert-output.sh [options]
```

#### Options

| Option | Type | Required | Description |
|--------|------|----------|-------------|
| --format | string | Yes | Target format: `html`, `pdf`, `word` |
| --input | string | Yes | Input file path |
| --output | string | Yes | Output file path |
| --style | string | No | Output style to apply |
| --template | string | No | Template for PDF/Word |

#### Examples

```bash
# Convert to HTML
.moai/scripts/convert-output.sh \
  --format html \
  --input report.md \
  --output report.html

# Convert to PDF with template
.moai/scripts/convert-output.sh \
  --format pdf \
  --input report.md \
  --output report.pdf \
  --template company-template

# Convert with style
.moai/scripts/convert-output.sh \
  --format word \
  --input analysis.md \
  --output analysis.docx \
  --style r2d2
```

#### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Conversion failed |
| 2 | Invalid parameters |
| 3 | Missing dependencies |

---

### validate-accessibility.sh

Validate HTML files for WCAG 2.1 AA compliance.

#### Syntax

```bash
.moai/scripts/validate-accessibility.sh [file]
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| file | string | Yes | HTML file to validate |

#### Examples

```bash
# Validate HTML file
.moai/scripts/validate-accessibility.sh report.html

# Expected output:
# ✓ WCAG 2.1 AA compliant
# ✓ Semantic HTML structure
# ✓ Keyboard navigation
# ✓ Screen reader compatibility
```

#### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All checks passed |
| 1 | Accessibility issues found |
| 2 | Invalid HTML |
| 3 | Missing dependencies |

---

## Output Style API

### Style Selection

Styles can be selected via:

1. **Command-line flag**: `--style moai`
2. **Configuration default**: `default_style: moai`
3. **Dynamic selection**: Based on task type

### Style Behaviors

#### MoAI Style

```markdown
🤖 MoAI ★ [Status] ─────────────────────────
📋 [Task Description]
⏳ [Action in progress]
────────────────────────────────────────────
```

**Characteristics**:
- Progress indicators
- Emoji decorations
- Bilingual support (if configured)
- Professional formatting

**Configuration**:
```yaml
styles:
  moai:
    language_aware: true
    show_progress: true
    emoji_decorations: true
```

#### R2D2 Style

```markdown
[STATUS] Processing...
[INPUT] Analyzing code structure
[OUTPUT] Found 3 files to process
[RESULT] Analysis complete
```

**Characteristics**:
- Bracketed tags
- Concise messages
- Code-focused
- Minimal formatting

**Configuration**:
```yaml
styles:
  r2d2:
    concise: true
    technical: true
    minimal_formatting: true
```

#### Yoda Style

```markdown
Hmm, let me analyze this situation carefully.

The code structure suggests... [detailed analysis]

A wise approach would be... [recommendation]

Think on this, you must. [closing]
```

**Characteristics**:
- Reflective language
- Strategic perspective
- Educational tone
- Thoughtful analysis

**Configuration**:
```yaml
styles:
  yoda:
    wisdom_focused: true
    strategic: true
    educational: true
```

---

## Format Conversion API

### Supported Formats

| Format | Input | Output | Dependencies |
|--------|-------|--------|--------------|
| Markdown | Yes | Yes | None |
| HTML | Yes | Yes | Pandoc |
| PDF | Yes | Yes | Pandoc, wkhtmltopdf |
| Word | Yes | Yes | Pandoc |

### Conversion Pipeline

```
Source Format
    ↓
[Format Converter]
    ↓
Style Application
    ↓
Template Processing
    ↓
Output Format
```

### Conversion Options

| Option | Type | Formats | Description |
|--------|------|---------|-------------|
| --css-theme | string | HTML | CSS theme to apply |
| --include-toc | boolean | HTML, PDF | Include table of contents |
| --bookmarks | boolean | PDF | Include PDF bookmarks |
| --template | string | PDF, Word | Template file to use |
| --track-changes | boolean | Word | Enable track changes |

---

## Error Handling

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `E001` | Missing dependencies | Install Pandoc/wkhtmltopdf |
| `E002` | Invalid format | Use supported format |
| `E003` | Template not found | Check template path |
| `E004` | Conversion failed | Check input file format |
| `E005` | Accessibility failed | Fix HTML issues |

### Error Response Format

```json
{
  "error": "E001",
  "message": "Missing required dependency: pandoc",
  "details": {
    "required": "pandoc >= 2.19",
    "install": "brew install pandoc"
  }
}
```

---

## Performance API

### Conversion Speed

| Format | Average Speed | Max Size |
|--------|---------------|----------|
| Markdown | Instant | Unlimited |
| HTML | <1s/MB | 50MB |
| PDF | 2-5s/MB | 100MB |
| Word | 5-10s/MB | 50MB |

### Optimization Options

```yaml
output:
  optimization:
    parallel_conversion: true    # Convert multiple files in parallel
    cache_intermediate: true     # Cache intermediate results
    compress_output: true        # Compress output files
    max_file_size: 104857600     # 100MB max file size
```

---

## Integration API

### Plugin Integration

Cowork Supervisor automatically applies output styles to results from all coordinated plugins.

```bash
# All plugin results formatted in R2D2 style
/supervise "Analyze technical stack" --style r2d2

# Results from Finance, Legal, Marketing plugins
# all formatted consistently in selected style
```

### Custom Plugins

Plugins can specify their preferred output format:

```json
{
  "name": "custom-plugin",
  "output": {
    "preferred_format": "html",
    "supported_styles": ["moai", "r2d2"],
    "custom_template": "plugin-template.html"
  }
}
```

---

## Version Information

### Current Version

- **Version**: 1.1.0
- **Release Date**: 2026-02-09
- **API Level**: 1

### Version Compatibility

| Cowork Supervisor | API Level | Status |
|------------------|-----------|--------|
| 1.0.x | 1 | Stable |
| 1.1.0 | 1 | Stable |

---

## Support

For API issues or questions:
- GitHub: https://github.com/team-attention/cowork-supervisor
- Issues: https://github.com/team-attention/cowork-supervisor/issues
- Documentation: See docs/OUTPUT_STYLES.md
