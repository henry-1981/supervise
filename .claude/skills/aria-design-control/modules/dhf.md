# DHF (Design History File)

Design History File 상세 가이드.

## DHF Purpose

DHF는 설계 프로젝트의 전체 이력을 포함하는 공식적인 문서 집합입니다.

### Regulatory Requirements

| 규제 | 요구사항 |
|------|----------|
| FDA 21 CFR 820.30(i) | DHF에 포함될 내용 명시 |
| FDA 21 CFR 820.30(j) | DHF 준비 및 유지 |
| FDA 21 CFR 820.30(a)-(h) | 각 설계 활동별 문서화 |

## DHF Structure

### 1. Design Plan (설계 계획)

#### Purpose
프로젝트의 범위, 일정, 조직을 정의합니다.

#### Contents

**1.1 Project Overview**
- Device name and description
- Intended use
- Indications for use
- Target market

**1.2 Development Schedule**
- Milestones
- Design reviews
- Verification activities
- Validation activities
- Transfer to production

**1.3 Team Roles and Responsibilities**
- Project manager
- Design engineers
- Quality assurance
- Regulatory affairs
- Clinical consultants

**1.4 Risk Management Integration**
- Risk management process [ISO 14971]
- Risk analysis timing
- Risk control measures
- Residual risk evaluation

### 2. Design Inputs (설계 입력)

#### Purpose
제품이 충족해야 할 요구사항을 정의합니다.

#### Contents

**2.1 User Needs**
- Clinical problems to be solved
- User requirements
- Patient requirements
- Healthcare provider requirements

**2.2 Intended Use**
- Primary intended use
- Secondary intended uses (if any)
- Contraindications
- Warnings and precautions

**2.3 Clinical Benefits**
- Intended clinical benefits
- Alternative treatments comparison
- Risk-benefit justification

**2.4 Regulatory Requirements**
- FDA classification (Class I, II, III)
- Regulatory pathway (510(k), PMA, De Novo)
- Predicate device (if applicable)
- Special controls (if Class II)

**2.5 Risk Management Inputs**
- Hazard identification
- Risk estimation
- Risk control priorities

### 3. Design Outputs (설계 출력)

#### Purpose
설계 입력을 충족하는 제품 명세서를 정의합니다.

#### Contents

**3.1 Product Specifications**
- Functional requirements
- Performance requirements
- Physical characteristics
- Environmental requirements

**3.2 Software Requirements** [IEC 62304]
- Software architecture
- Software safety class
- Functional specifications
- Interface specifications

**3.3 Hardware Specifications**
- Electronic components
- Mechanical components
- Materials
- Tolerances

**3.4 Labeling and IFU**
- Device labeling
- Instructions for Use
- Symbols and graphics
- Warnings and precautions

**3.5 Packaging Specifications**
- Primary packaging
- Secondary packaging
- Shipping container
- Sterility (if applicable)

### 4. Design Reviews (설계 검토)

#### Purpose
설계의 적절성을 평가하고 승인합니다.

#### Types of Design Reviews

**4.1 Concept Review**
- Feasibility assessment
- Technology selection
- Preliminary risk assessment

**4.2 Critical Design Review**
- Design completeness
- Risk control effectiveness
- Verification readiness

**4.3 Verification Review**
- Verification results review
- Design adequacy assessment
- Validation readiness

**4.4 Validation Review**
- Validation results review
- Clinical acceptance
- Production readiness

#### Design Review Requirements [21 CFR 820.30(d)]

- Formal, documented, consistent
- Include independent reviewers
- Document results and decisions
- Maintain records in DHF

### 5. Design Verification (설계 검증)

#### Purpose
설계 출력이 설계 입력을 충족하는지 확인합니다.

#### Verification Methods [21 CFR 820.30(e)]

1. **Inspection**: Visual examination, measurement
2. **Analysis**: Mathematical modeling, simulation
3. **Testing**: Performance testing, stress testing
4. **Demonstration**: Functional demonstration

#### Verification Documentation

**5.1 Test Protocols**
- Test objective
- Test procedure
- Acceptance criteria
- Test equipment

**5.2 Test Results**
- Raw data
- Analysis results
- Pass/fail determination
- Deviations (if any)

**5.3 Analysis Reports**
- Statistical analysis
- Trend analysis
- Comparison to specifications

### 6. Design Validation (설계 유효성 확인)

#### Purpose
제품이 의도된 사용에 적합한지 확인합니다.

#### Validation Methods [21 CFR 820.30(f)]

1. **Clinical Investigation**: Human subjects study
2. **Literature Review**: Published clinical data
3. **Predicate Device Comparison**: Equivalence assessment
4. **User Testing**: Usability testing [IEC 62366-1]

#### Validation Documentation

**6.1 Clinical Evaluation**
- Clinical investigation plan
- Clinical data collection
- Statistical analysis
- Clinical evaluation report

**6.2 Usability Testing** [IEC 62366-1]
- Use scenarios
- User groups
- Task success rates
- Error analysis

**6.3 Validation Summary**
- Clinical acceptance
- Risk-benefit assessment
- Overall conclusions

### 7. Design Transfer (설계 이관)

#### Purpose
설계를 생산으로 이관합니다.

#### Transfer Activities [21 CFR 820.30(g)]

**7.1 DMR Completion**
- Production specifications
- Quality procedures
- Packaging and labeling
- Installation and servicing

**7.2 Process Validation**
- Manufacturing process validation
- Equipment qualification (IQ/OQ/PQ)
- Process capability studies

**7.3 Production Readiness**
- First article inspection
- Pilot production run
- DHR generation

### 8. Design Changes (설계 변경)

#### Purpose
설계 변경을 통제하고 문서화합니다.

#### Change Process [21 CFR 820.30(h)]

**8.1 Change Requests**
- Change justification
- Impact assessment
- Risk analysis update

**8.2 Change Implementation**
- Verification of changes
- Validation of changes
- Regulatory assessment (if needed)

**8.3 Change Approval**
- Design review
- Final approval
- DHF update

## DHF Template

```markdown
# DHF-[DEVICE-ID]-[REVISION]: [Device Name] Design History File

## 1.0 Design Plan
### 1.1 Project Overview
- Device Name: [Name]
- Device ID: [ID]
- Intended Use: [Description]
- Classification: [Class I/II/III]
- Regulatory Pathway: [510(k)/PMA/De Novo]

### 1.2 Development Schedule
| Milestone | Target Date | Actual Date | Status |
|-----------|-------------|-------------|--------|
| Concept Review | YYYY-MM-DD | YYYY-MM-DD | Complete |
| Critical Design Review | YYYY-MM-DD | YYYY-MM-DD | Complete |
| Verification Complete | YYYY-MM-DD | YYYY-MM-DD | In Progress |
| Validation Complete | YYYY-MM-DD | YYYY-MM-DD | Pending |

### 1.3 Team Roles
| Role | Name | Qualifications |
|------|------|----------------|
| Project Manager | | |
| Design Engineer | | |
| Quality Assurance | | |
| Regulatory Affairs | | |

## 2.0 Design Inputs
### 2.1 User Needs
| Need ID | User Need | Source | Priority |
|---------|-----------|--------|----------|
| UN-001 | [Description] | [Interview/Survey] | High |

### 2.2 Intended Use
- Primary: [Description]
- Indications: [List]
- Contraindications: [List]

### 2.3 Clinical Benefits
| Benefit | Evidence Source |
|---------|-----------------|
| [Description] | [Literature/Clinical data] |

### 2.4 Regulatory Requirements
- Classification: [Class]
- Predicate: [Device name, 510(k) number]
- Standards: [ISO 13485, ISO 14971, etc.]

## 3.0 Design Outputs
### 3.1 Product Specifications
| Spec ID | Specification | Requirement ID |
|---------|---------------|----------------|
| PS-001 | [Description] | UN-001 |

### 3.2 Software Requirements [IEC 62304]
| Req ID | Requirement | Safety Class |
|--------|-------------|---------------|
| SR-001 | [Description] | [A/B/C] |

## 4.0 Design Reviews
### 4.1 Concept Review
- Date: YYYY-MM-DD
- Attendees: [List]
- Decisions: [Summary]
- Action Items: [List]

## 5.0 Design Verification
### 5.1 Test Protocols
| Test ID | Test Description | Acceptance Criteria |
|---------|-----------------|---------------------|
| VT-001 | [Description] | [Criteria] |

### 5.2 Test Results
| Test ID | Result | Pass/Fail | Comments |
|---------|--------|-----------|----------|
| VT-001 | [Data] | Pass | |

## 6.0 Design Validation
### 6.1 Clinical Evaluation
- Study Design: [Description]
- Sample Size: [N]
- Results: [Summary]
- Conclusions: [Accept/Reject]

## 7.0 Design Transfer
### 7.1 DMR Status
- DMR Number: [DMR-ID]
- Status: [Complete/In Progress]
- Transfer Date: YYYY-MM-DD

## 8.0 Design Changes
### 8.1 Change Log
| Change ID | Description | Date | Approval |
|-----------|-------------|------|----------|
| DC-001 | [Description] | YYYY-MM-DD | Approved |
```

## DHF Best Practices

### Documentation

1. **Write as you go**
   - Don't wait until the end
   - Document decisions immediately
   - Keep records current

2. **Use templates**
   - Consistent format
   - Complete sections
   - Easy to review

3. **Version control**
   - Track all changes
   - Maintain revision history
   - Document rationale

### Review Process

1. **Independent reviewers**
   - Subject matter experts
   - Quality assurance
   - Regulatory affairs

2. **Document decisions**
   - What was decided
   - Why it was decided
   - Alternatives considered

3. **Track action items**
   - Assign responsibilities
   - Set due dates
   - Verify completion

## Common DHF Mistakes

### 1. Incomplete Design Inputs
- **Problem**: Missing user needs or regulatory requirements
- **Solution**: Use comprehensive input checklist

### 2. Missing Links
- **Problem**: Design outputs not linked to inputs
- **Solution**: Maintain traceability matrix

### 3. Incomplete Verification
- **Problem**: Not all outputs verified
- **Solution**: Verify completeness before moving to validation

### 4. Inadequate Validation
- **Problem**: Validation doesn't cover intended use
- **Solution**: Comprehensive clinical validation plan

## References

- FDA 21 CFR 820.30 - Design Controls
- ISO 13485:2016 Section 7.3 - Design and Development
- IEC 62304 - Medical Device Software Life Cycle
- IEC 62366-1 - Usability Engineering
