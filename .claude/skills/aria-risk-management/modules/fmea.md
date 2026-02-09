# FMEA (Failure Mode and Effects Analysis)

## Overview

FMEA is a bottom-up, systematic method for identifying potential failures in a system, product, or process.

## FMEA Process

### Step 1: Identify Failure Modes

**Process:**
- List all components and functions
- Identify ways each component could fail
- Consider all potential failure modes

**Common Failure Modes:**
- No function (failure to operate)
- Partial function (reduced performance)
- Intermittent function (unreliable operation)
- Unintended function (operates when not supposed to)

### Step 2: Determine Effects

**For Each Failure Mode:**
- Identify local effects (component level)
- Identify system effects (device level)
- Identify user effects (patient level)

**Severity Rating Scale:**
- 1: Negligible (inconvenient or temporary impairment)
- 2: Minor (requires professional medical intervention)
- 3: Moderate (requires hospitalization or intervention)
- 4: Serious (permanent impairment or life-threatening)
- 5: Catastrophic (death)

### Step 3: Identify Causes

**Process:**
- Determine root causes of each failure mode
- Use techniques like 5 Whys, Fishbone diagram

**Common Causes:**
- Design defects
- Material failures
- Manufacturing defects
- Environmental conditions
- User error

**Occurrence Rating Scale:**
- 1: Remote (< 10^-6 per year)
- 2: Low (10^-6 to 10^-4 per year)
- 3: Medium (10^-4 to 10^-2 per year)
- 4: High (10^-2 to 10^-1 per year)
- 5: Frequent (> 10^-1 per year)

### Step 4: Identify Controls

**Detection Methods:**
- Design verification
- Process validation
- Testing procedures
- Quality inspections

**Detection Rating Scale:**
- 1: Certain (detectable before failure)
- 2: High (almost certain detection)
- 3: Moderate (moderate chance of detection)
- 4: Low (low chance of detection)
- 5: Uncertain (undetectable)

### Step 5: Calculate RPN

**Risk Priority Number = Severity × Occurrence × Detection**

**RPN Scale:**
- 1-50: Low risk
- 51-100: Moderate risk
- 101-125: High risk
- >125: Very high risk

### Step 6: Prioritize Actions

**RPN Threshold:**
- RPN > 100: Immediate action required
- RPN 50-100: Action within 30 days
- RPN < 50: Monitor and review

---

**Version:** 1.0.0
**Last Updated:** 2026-02-09
**Reference:** [ISO 14971:2019] Annex C
