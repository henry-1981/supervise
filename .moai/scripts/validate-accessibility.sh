#!/bin/bash
# ARIA Accessibility Validation Script
# Validates output documents for WCAG 2.1 AA and PDF/UA compliance

set -e

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
}

# Validation results tracking
PASSED_CHECKS=0
FAILED_CHECKS=0
WARNED_CHECKS=0

# WCAG 2.1 AA Validation Functions
validate_html_accessibility() {
    local html_file=$1

    log_info "Validating HTML for WCAG 2.1 AA compliance: $html_file"

    # Check 1: Language attribute
    if grep -q 'lang=' "$html_file"; then
        log_pass "Language attribute present"
        ((PASSED_CHECKS++))
    else
        log_fail "Missing lang attribute on html element"
        ((FAILED_CHECKS++))
    fi

    # Check 2: Document title
    if grep -q '<title>' "$html_file"; then
        log_pass "Document title present"
        ((PASSED_CHECKS++))
    else
        log_fail "Missing document title"
        ((FAILED_CHECKS++))
    fi

    # Check 3: Heading structure
    local heading_count=$(grep -cE '<h[1-6]' "$html_file" || true)
    if [ "$heading_count" -gt 0 ]; then
        log_pass "Headings found ($heading_count headings)"
        ((PASSED_CHECKS++))

        # Check heading hierarchy
        local h1_count=$(grep -c '<h1' "$html_file" || true)
        if [ "$h1_count" -eq 1 ]; then
            log_pass "Exactly one H1 heading"
            ((PASSED_CHECKS++))
        else
            log_warn "Expected exactly one H1 heading, found $h1_count"
            ((WARNED_CHECKS++))
        fi
    else
        log_warn "No headings found"
        ((WARNED_CHECKS++))
    fi

    # Check 4: Alt text for images
    local img_count=$(grep -c '<img' "$html_file" || true)
    local img_without_alt=$(grep -cE '<img[^>]*(?!alt=)' "$html_file" || true)
    if [ "$img_count" -gt 0 ]; then
        if [ "$img_without_alt" -eq 0 ]; then
            log_pass "All images have alt text"
            ((PASSED_CHECKS++))
        else
            log_fail "$img_without_alt images missing alt text"
            ((FAILED_CHECKS++))
        fi
    fi

    # Check 5: Link descriptiveness
    local generic_links=$(grep -cE '<a[^>]*>(here|click here|read more)</a>' "$html_file" || true)
    if [ "$generic_links" -eq 0 ]; then
        log_pass "No generic link text found"
        ((PASSED_CHECKS++))
    else
        log_warn "$generic_links generic link texts found"
        ((WARNED_CHECKS++))
    fi

    # Check 6: Table headers
    if grep -q '<table' "$html_file"; then
        local th_count=$(grep -c '<th' "$html_file" || true)
        if [ "$th_count" -gt 0 ]; then
            log_pass "Table headers present"
            ((PASSED_CHECKS++))

            # Check for scope attribute
            local th_with_scope=$(grep -cE '<th[^>]*scope=' "$html_file" || true)
            if [ "$th_with_scope" -gt 0 ]; then
                log_pass "Table headers have scope attributes"
                ((PASSED_CHECKS++))
            else
                log_warn "Table headers missing scope attributes"
                ((WARNED_CHECKS++))
            fi
        else
            log_fail "Table found but no table headers"
            ((FAILED_CHECKS++))
        fi
    fi

    # Check 7: Form labels
    if grep -qE '<input|<select|<textarea' "$html_file"; then
        local input_count=$(grep -cE '<input|<select|<textarea' "$html_file" || true)
        local label_count=$(grep -c '<label' "$html_file" || true)
        if [ "$label_count" -ge "$input_count" ]; then
            log_pass "Form inputs have labels"
            ((PASSED_CHECKS++))
        else
            log_fail "Some form inputs missing labels"
            ((FAILED_CHECKS++))
        fi
    fi

    # Check 8: Skip navigation link
    if grep -qE 'skip.*navigation|skip.*content' "$html_file"; then
        log_pass "Skip navigation link present"
        ((PASSED_CHECKS++))
    else
        log_warn "Skip navigation link not found"
        ((WARNED_CHECKS++))
    fi

    # Check 9: Color contrast (basic check)
    # This would require more sophisticated tools in production
    log_info "Color contrast check requires visual validation"
    ((WARNED_CHECKS++))

    # Check 10: ARIA attributes
    local aria_count=$(grep -c 'aria-' "$html_file" || true)
    if [ "$aria_count" -gt 0 ]; then
        log_pass "ARIA attributes found ($aria_count attributes)"
        ((PASSED_CHECKS++))
    else
        log_warn "No ARIA attributes found"
        ((WARNED_CHECKS++))
    fi

    log_info "HTML validation complete: $PASSED_CHECKS passed, $FAILED_CHECKS failed, $WARNED_CHECKS warnings"
}

# PDF/UA Validation Functions
validate_pdf_accessibility() {
    local pdf_file=$1

    log_info "Validating PDF for PDF/UA compliance: $pdf_file"

    # Check if file exists
    if [ ! -f "$pdf_file" ]; then
        log_fail "PDF file not found: $pdf_file"
        return 1
    fi

    # Check 1: File size (basic sanity check)
    local file_size=$(stat -f%z "$pdf_file" 2>/dev/null || stat -c%s "$pdf_file" 2>/dev/null || echo 0)
    if [ "$file_size" -gt 0 ]; then
        log_pass "PDF file exists and has content ($file_size bytes)"
        ((PASSED_CHECKS++))
    else
        log_fail "PDF file is empty or invalid"
        ((FAILED_CHECKS++))
        return 1
    fi

    # Check 2: PDF version (requires pdffonts or similar)
    if command -v pdffonts &> /dev/null; then
        log_info "Checking PDF structure with pdffonts"
        pdffonts "$pdf_file" > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            log_pass "PDF structure is valid"
            ((PASSED_CHECKS++))
        else
            log_fail "PDF structure is invalid"
            ((FAILED_CHECKS++))
        fi
    else
        log_warn "pdffonts not available - skipping structure check"
        ((WARNED_CHECKS++))
    fi

    # Check 3: Tagged PDF (requires detailed PDF analysis)
    log_info "Tagged PDF check requires specialized tools (e.g., pdfua-validator, Adobe Acrobat)"
    ((WARNED_CHECKS++))

    # Check 4: Metadata
    if command -v pdfinfo &> /dev/null; then
        local title=$(pdfinfo "$pdf_file" | grep "Title:" | cut -d: -f2 | xargs)
        if [ -n "$title" ]; then
            log_pass "PDF title metadata present: $title"
            ((PASSED_CHECKS++))
        else
            log_warn "PDF title metadata missing"
            ((WARNED_CHECKS++))
        fi
    else
        log_warn "pdfinfo not available - skipping metadata check"
        ((WARNED_CHECKS++))
    fi

    # Check 5: Embedded fonts (basic check)
    if command -v pdffonts &> /dev/null; then
        local embedded_fonts=$(pdffonts "$pdf_file" 2>/dev/null | grep -c "yes" || true)
        if [ "$embedded_fonts" -gt 0 ]; then
            log_pass "Embedded fonts found ($embedded_fonts fonts)"
            ((PASSED_CHECKS++))
        else
            log_warn "No embedded fonts found"
            ((WARNED_CHECKS++))
        fi
    fi

    log_info "PDF validation complete: $PASSED_CHECKS passed, $FAILED_CHECKS failed, $WARNED_CHECKS warnings"
}

# Word Document Validation
validate_word_accessibility() {
    local docx_file=$1

    log_info "Validating Word document for accessibility: $docx_file"

    # Check if file exists
    if [ ! -f "$docx_file" ]; then
        log_fail "Word file not found: $docx_file"
        return 1
    fi

    # Check 1: File size
    local file_size=$(stat -f%z "$docx_file" 2>/dev/null || stat -c%s "$docx_file" 2>/dev/null || echo 0)
    if [ "$file_size" -gt 1000 ]; then
        log_pass "Word file has reasonable size ($file_size bytes)"
        ((PASSED_CHECKS++))
    else
        log_fail "Word file is too small or invalid"
        ((FAILED_CHECKS++))
        return 1
    fi

    # Check 2: ZIP structure (docx is a ZIP file)
    if command -v unzip &> /dev/null; then
        unzip -t "$docx_file" > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            log_pass "Word file structure is valid"
            ((PASSED_CHECKS++))
        else
            log_fail "Word file structure is invalid"
            ((FAILED_CHECKS++))
        fi
    else
        log_warn "unzip not available - skipping structure check"
        ((WARNED_CHECKS++))
    fi

    # Note: Full Word accessibility validation requires specialized tools
    # like Microsoft Word's Accessibility Checker or python-docx
    log_info "Full Word accessibility validation requires specialized tools"
    ((WARNED_CHECKS++))

    log_info "Word validation complete: $PASSED_CHECKS passed, $FAILED_CHECKS failed, $WARNED_CHECKS warnings"
}

# Generate validation report
generate_report() {
    local output_file=$1
    local total_checks=$((PASSED_CHECKS + FAILED_CHECKS + WARNED_CHECKS))

    cat > "$output_file" << EOF
# ARIA Accessibility Validation Report

Generated: $(date)
Document: $2

## Summary

- Total Checks: $total_checks
- Passed: $PASSED_CHECKS
- Failed: $FAILED_CHECKS
- Warnings: $WARNED_CHECKS

## Compliance Status

EOF

    if [ $FAILED_CHECKS -eq 0 ]; then
        echo "✅ PASSED - Document meets accessibility requirements" >> "$output_file"
    else
        echo "❌ FAILED - Document does not meet accessibility requirements" >> "$output_file"
    fi

    if [ $WARNED_CHECKS -gt 0 ]; then
        echo "⚠️  WARNINGS - Manual review recommended for $WARNED_CHECKS items" >> "$output_file"
    fi

    cat >> "$output_file" << EOF

## Standards

- WCAG 2.1 AA: Web Content Accessibility Guidelines
- PDF/UA: Universal Accessibility PDF Standard

## Recommendations

1. Address all failed checks
2. Review warnings manually
3. Test with screen readers (NVDA, JAWS)
4. Validate with automated tools (axe, WAVE)
5. Conduct user testing with assistive technology

## Tools Used

- ARIA Accessibility Validation Script v1.0
- Platform: $(uname -s)
- Date: $(date +%Y-%m-%d)

---

This report was generated automatically by the ARIA format conversion pipeline.
EOF

    log_info "Validation report written to: $output_file"
}

# Script usage
usage() {
    cat << EOF
ARIA Accessibility Validation Script

Usage: $0 [OPTIONS] FILE OUTPUT_FORMAT [REPORT_FILE]

Arguments:
  FILE                Input document file to validate
  OUTPUT_FORMAT       Format type (html, pdf, word)
  REPORT_FILE         Optional output report file (default: accessibility-report.md)

Options:
  -h, --help          Show this help message
  -v, --verbose       Enable verbose output
  -s, --strict        Treat warnings as failures

Examples:
  $0 document.html html
  $0 document.pdf pdf accessibility-report.md
  $0 document.docx word --strict

Exit Codes:
  0                   All checks passed
  1                   Some checks failed
  2                   Validation error occurred

EOF
}

# Main script execution
main() {
    local input_file=""
    local output_format=""
    local report_file=""
    local verbose=false
    local strict=false

    # Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                exit 0
                ;;
            -v|--verbose)
                verbose=true
                shift
                ;;
            -s|--strict)
                strict=true
                shift
                ;;
            -*)
                echo "Error: Unknown option: $1"
                usage
                exit 2
                ;;
            *)
                if [ -z "$input_file" ]; then
                    input_file="$1"
                elif [ -z "$output_format" ]; then
                    output_format="$1"
                elif [ -z "$report_file" ]; then
                    report_file="$1"
                else
                    echo "Error: Too many arguments"
                    usage
                    exit 2
                fi
                shift
                ;;
        esac
    done

    # Validate required arguments
    if [ -z "$input_file" ] || [ -z "$output_format" ]; then
        echo "Error: Missing required arguments"
        usage
        exit 2
    fi

    # Check if input file exists
    if [ ! -f "$input_file" ]; then
        echo "Error: Input file not found: $input_file"
        exit 2
    fi

    # Set default report file if not provided
    if [ -z "$report_file" ]; then
        report_file="$(dirname "$input_file")/accessibility-report.md"
    fi

    # Route to appropriate validation function
    case "$output_format" in
        html|HTML)
            validate_html_accessibility "$input_file"
            ;;
        pdf|PDF)
            validate_pdf_accessibility "$input_file"
            ;;
        word|docx|DOCX)
            validate_word_accessibility "$input_file"
            ;;
        *)
            echo "Error: Unsupported format: $output_format"
            usage
            exit 2
            ;;
    esac

    # Generate report
    generate_report "$report_file" "$input_file"

    # Determine exit code
    if [ $FAILED_CHECKS -gt 0 ]; then
        exit 1
    elif [ "$strict" = true ] && [ $WARNED_CHECKS -gt 0 ]; then
        exit 1
    else
        exit 0
    fi
}

# Run main function
main "$@"
