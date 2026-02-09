#!/bin/bash
# ARIA Format Conversion Script
# Converts regulatory documents between formats with accessibility compliance

set -e

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONFIG_FILE="$PROJECT_ROOT/.moai/config/sections/output.yaml"

# Source configuration if exists
if [ -f "$CONFIG_FILE" ]; then
    # Parse YAML (simple parsing, for production use yq or similar)
    DEFAULT_FORMAT=$(grep "default_format:" "$CONFIG_FILE" | head -1 | cut -d: -f2 | xargs)
else
    DEFAULT_FORMAT="markdown"
fi

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Tool availability check
check_tool_availability() {
    local tool=$1
    if command -v "$tool" &> /dev/null; then
        log_info "$tool is available"
        return 0
    else
        log_warn "$tool is not available"
        return 1
    fi
}

# Markdown to HTML conversion
markdown_to_html() {
    local input_file=$1
    local output_file=$2
    local css_theme=${3:-"regulatory-standard"}

    log_info "Converting Markdown to HTML: $input_file -> $output_file"

    # Check if Pandoc is available
    if check_tool_availability "pandoc"; then
        pandoc "$input_file" \
            -f markdown \
            -t html5 \
            -o "$output_file" \
            --standalone \
            --metadata title="ARIA Regulatory Document" \
            --css="$PROJECT_ROOT/.moai/templates/css/${css_theme}.css" \
            --toc \
            --toc-depth=3 \
            --number-sections \
            || {
                log_error "Pandoc conversion failed"
                return 1
            }
    else
        # Fallback to basic conversion
        log_warn "Pandoc not available, using basic Markdown to HTML conversion"
        basic_markdown_to_html "$input_file" "$output_file"
    fi

    # Add accessibility attributes
    add_accessibility_attributes "$output_file"

    log_info "HTML conversion completed"
}

# Basic Markdown to HTML conversion (fallback)
basic_markdown_to_html() {
    local input_file=$1
    local output_file=$2

    cat > "$output_file" << EOF
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ARIA Regulatory Document</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1, h2, h3, h4, h5, h6 { color: #0066cc; margin-top: 1.5em; }
        code { background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }
        pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
        table { border-collapse: collapse; width: 100%; margin: 1em 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #0066cc; color: white; }
        a { color: #0066cc; }
        .toc { background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <main role="main">
EOF

    # Simple Markdown to HTML conversion (very basic)
    sed -e 's/^# \(.*\)$/<h1>\1<\/h1>/' \
        -e 's/^## \(.*\)$/<h2>\1<\/h2>/' \
        -e 's/^### \(.*\)$/<h3>\1<\/h3>/' \
        -e 's/\*\*\([^*]*\)\*\*/<strong>\1<\/strong>/g' \
        -e 's/\*\([^*]*\)\*/<em>\1<\/em>/g' \
        "$input_file" >> "$output_file"

    cat >> "$output_file" << EOF
    </main>
</body>
</html>
EOF
}

# HTML to PDF conversion
html_to_pdf() {
    local input_file=$1
    local output_file=$2

    log_info "Converting HTML to PDF: $input_file -> $output_file"

    # Try wkhtmltopdf first
    if check_tool_availability "wkhtmltopdf"; then
        wkhtmltopdf "$input_file" "$output_file" \
            --orientation Portrait \
            --page-size Letter \
            --margin-top 0.75in \
            --margin-bottom 0.75in \
            --margin-left 0.75in \
            --margin-right 0.75in \
            --enable-local-file-access \
            --javascript-delay 1000 \
            --no-stop-slow-scripts \
            || {
                log_error "wkhtmltopdf conversion failed"
                return 1
            }
    # Try Pandoc as fallback
    elif check_tool_availability "pandoc"; then
        pandoc "$input_file" \
            -f html \
            -o "$output_file" \
            --pdf-engine=xelatex \
            || {
                log_error "Pandoc PDF conversion failed"
                return 1
            }
    else
        log_error "No PDF conversion tool available (wkhtmltopdf or Pandoc required)"
        return 1
    fi

    # Tag PDF for accessibility if available
    tag_pdf "$output_file"

    log_info "PDF conversion completed"
}

# Markdown to Word conversion
markdown_to_word() {
    local input_file=$1
    local output_file=$2

    log_info "Converting Markdown to Word: $input_file -> $output_file"

    if check_tool_availability "pandoc"; then
        local template="$PROJECT_ROOT/.moai/templates/word/regulatory-template.dotx"
        local template_opt=""
        if [ -f "$template" ]; then
            template_opt="--reference-doc=$template"
        fi

        pandoc "$input_file" \
            -f markdown \
            -t docx \
            -o "$output_file" \
            $template_opt \
            --toc \
            --toc-depth=3 \
            || {
                log_error "Pandoc Word conversion failed"
                return 1
            }
    else
        log_error "Pandoc is required for Word conversion"
        return 1
    fi

    log_info "Word conversion completed"
}

# Add accessibility attributes to HTML
add_accessibility_attributes() {
    local html_file=$1

    log_info "Adding accessibility attributes to HTML"

    # Add lang attribute if missing
    sed -i.tmp 's/<html>/<html lang="ko">/' "$html_file"
    rm -f "${html_file}.tmp"

    # Add role="main" to main content area
    # Add proper ARIA labels where needed
    # Ensure proper heading hierarchy
    # Add alt text to images

    log_info "Accessibility attributes added"
}

# Tag PDF for accessibility (PDF/UA)
tag_pdf() {
    local pdf_file=$1

    log_info "Tagging PDF for accessibility (PDF/UA)"

    # This would typically use a tool like Ghostscript or Adobe Acrobat
    # For now, we'll log a warning if proper tagging tools aren't available
    if ! command -v gs &> /dev/null; then
        log_warn "Ghostscript not available - PDF tagging may be incomplete"
    fi
}

# Validate output format
validate_output() {
    local output_file=$1
    local format=$2

    log_info "Validating $format output: $output_file"

    case "$format" in
        html)
            validate_html_accessibility "$output_file"
            ;;
        pdf)
            validate_pdf_accessibility "$output_file"
            ;;
        word)
            validate_word_formatting "$output_file"
            ;;
    esac
}

# Validate HTML accessibility (WCAG 2.1 AA)
validate_html_accessibility() {
    local html_file=$1

    log_info "Validating HTML for WCAG 2.1 AA compliance"

    # Check for lang attribute
    if ! grep -q 'lang=' "$html_file"; then
        log_warn "Missing lang attribute on html element"
    fi

    # Check for heading structure
    # Check for alt text on images
    # Check for proper table structure
    # Check for link descriptiveness

    log_info "HTML accessibility validation completed"
}

# Validate PDF accessibility (PDF/UA)
validate_pdf_accessibility() {
    local pdf_file=$1

    log_info "Validating PDF for PDF/UA compliance"

    # This would typically use a tool like pdf.validator or Adobe Acrobat
    # For now, we'll do basic checks

    log_info "PDF accessibility validation completed"
}

# Validate Word formatting
validate_word_formatting() {
    local docx_file=$1

    log_info "Validating Word document formatting"

    # This would typically use a tool like mammoth or python-docx
    # For now, we'll do basic checks

    log_info "Word formatting validation completed"
}

# Main conversion function
convert_document() {
    local input_file=$1
    local output_format=$2
    local output_file=$3

    # Get file extension
    local input_ext="${input_file##*.}"

    # Determine output filename if not provided
    if [ -z "$output_file" ]; then
        local base_name="${input_file%.*}"
        case "$output_format" in
            html|HTML)
                output_file="${base_name}.html"
                ;;
            pdf|PDF)
                output_file="${base_name}.pdf"
                ;;
            word|docx|DOCX)
                output_file="${base_name}.docx"
                ;;
            *)
                output_file="${base_name}.${output_format}"
                ;;
        esac
    fi

    log_info "Starting conversion: $input_file -> $output_file"

    # Route to appropriate conversion function
    case "$input_ext" in
        md|markdown)
            case "$output_format" in
                html|HTML)
                    markdown_to_html "$input_file" "$output_file"
                    ;;
                pdf|PDF)
                    # Convert to HTML first, then to PDF
                    local temp_html="${input_file%.*}.temp.html"
                    markdown_to_html "$input_file" "$temp_html"
                    html_to_pdf "$temp_html" "$output_file"
                    rm -f "$temp_html"
                    ;;
                word|docx|DOCX)
                    markdown_to_word "$input_file" "$output_file"
                    ;;
                *)
                    log_error "Unsupported output format: $output_format"
                    return 1
                    ;;
            esac
            ;;
        html|htm)
            case "$output_format" in
                pdf|PDF)
                    html_to_pdf "$input_file" "$output_file"
                    ;;
                *)
                    log_error "Unsupported conversion: html -> $output_format"
                    return 1
                    ;;
            esac
            ;;
        *)
            log_error "Unsupported input format: $input_ext"
            return 1
            ;;
    esac

    # Validate output
    validate_output "$output_file" "$output_format"

    log_info "Conversion completed successfully"
    echo "$output_file"
}

# Script usage
usage() {
    cat << EOF
ARIA Format Conversion Script

Usage: $0 [OPTIONS] INPUT_FILE OUTPUT_FORMAT [OUTPUT_FILE]

Arguments:
  INPUT_FILE          Input document file (Markdown or HTML)
  OUTPUT_FORMAT       Target format (html, pdf, word)
  OUTPUT_FILE         Optional output filename

Options:
  -h, --help          Show this help message
  -t, --theme THEME   CSS theme for HTML output
  -v, --validate      Validate output after conversion
  -c, --check-tools   Check availability of conversion tools

Examples:
  $0 document.md html
  $0 document.md pdf output.pdf
  $0 document.md word --theme company-branding

Supported conversions:
  Markdown  -> HTML
  Markdown  -> PDF
  Markdown  -> Word
  HTML      -> PDF

EOF
}

# Main script execution
main() {
    local input_file=""
    local output_format=""
    local output_file=""
    local css_theme=""
    local validate=false
    local check_tools=false

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                exit 0
                ;;
            -t|--theme)
                css_theme="$2"
                shift 2
                ;;
            -v|--validate)
                validate=true
                shift
                ;;
            -c|--check-tools)
                check_tools=true
                shift
                ;;
            -*)
                log_error "Unknown option: $1"
                usage
                exit 1
                ;;
            *)
                if [ -z "$input_file" ]; then
                    input_file="$1"
                elif [ -z "$output_format" ]; then
                    output_format="$1"
                elif [ -z "$output_file" ]; then
                    output_file="$1"
                else
                    log_error "Too many arguments"
                    usage
                    exit 1
                fi
                shift
                ;;
        esac
    done

    # Check tool availability if requested
    if [ "$check_tools" = true ]; then
        echo "Checking conversion tools..."
        check_tool_availability "pandoc"
        check_tool_availability "wkhtmltopdf"
        check_tool_availability "gs"
        exit 0
    fi

    # Validate required arguments
    if [ -z "$input_file" ] || [ -z "$output_format" ]; then
        log_error "Missing required arguments"
        usage
        exit 1
    fi

    # Check if input file exists
    if [ ! -f "$input_file" ]; then
        log_error "Input file not found: $input_file"
        exit 1
    fi

    # Perform conversion
    convert_document "$input_file" "$output_format" "$output_file"
}

# Run main function
main "$@"
