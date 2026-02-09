# EU MDR Classification Rules

## Rule Structure

MDR Classification은 총 22개 규칙 (Rule 1-22)으로 구성됩니다. 위험도가 낮은 순서부터 높은 순서로 배열됩니다.

## Key Determinants

1. **Invasiveness**: Non-invasive → Invasively → Surgically invasive
2. **Duration**: Transient (< 60 min) → Short term (60 min - 30 days) → Long term (> 30 days)
3. **Body System**: Non-central nervous system → Central nervous system → Heart → Central circulatory system
4. **Active/Inactive**: Non-active → Active

## Rule Summary

### Non-invasive Devices (Rules 1-4)

**Rule 1: Non-invasive devices**
- Class I: Most non-invasive devices
- Examples: Wheelchairs, glasses, compression garments

**Rule 2: Non-invasive devices - Transient/Short term use**
- Class IIa: In contact with injured skin
- Class I: Intact skin contact
- Examples: Wound dressings, adhesive tapes

**Rule 3: Non-invasive devices - Long term use**
- Class IIa: Body orifices (except surgically invasive)
- Class IIb: Long term use > 30 days in orifices
- Examples: Contact lenses, hearing aids

**Rule 4: Non-invasive active devices**
- Class IIa: Low risk active devices
- Class IIb: Diagnosis, monitoring, conversion of signals
- Examples: Thermometers, blood pressure monitors

### Invasive Devices (Rules 5-8)

**Rule 5: Invasive devices - Body orifices**
- Class I: Transient use
- Class IIa: Short term use
- Class IIb: Long term use
- Examples: Specula, probes

**Rule 6: Surgically invasive - Transient use**
- Class II: Most transient surgical instruments
- Exceptions: Rule 8 (reusable surgical instruments → Class I)

**Rule 7: Surgically invasive - Short/Long term**
- Class IIa: Short term, except specific organs
- Class IIb: Long term, except specific organs
- Class III: Heart, central circulatory system, CNS

**Rule 8: Reusable surgical instruments**
- Class I: All reusable surgical instruments
- Examples: Scalpels, forceps, retractors

### Active Devices (Rules 9-12)

**Rule 9: Active therapeutic devices**
- Class IIa: Low risk
- Class IIb: Medium risk
- Class III: High risk (heart, CNS)
- Examples: Physiotherapy devices, lasers

**Rule 10: Active devices for diagnosis**
- Class IIa: Low risk
- Class IIb: Medium risk
- Examples: X-ray diagnostic equipment, ultrasound

**Rule 11: Active devices for therapy & diagnosis**
- Class III: Administering/exchanging energy to heart/CNS
- Examples: Defibrillators, pacemaker programmers

**Rule 12: Active devices for administering medicines**
- Class IIa: Low risk
- Class IIb: Medium/High risk
- Examples: Infusion pumps, nebulizers

### Special Rules (Rules 13-22)

**Rule 13: All other invasive devices**
- Class IIb: Not covered by other rules
- Examples: Most long-term implants

**Rule 14: Blood/Body fluid contact**
- Class IIb: Contact with blood
- Examples: Blood bags, blood collection sets

**Rule 15: Human origin tissues/cells**
- Class III: All devices incorporating human tissues/cells
- Examples: Tissue-engineered products

**Rule 16: Animal origin tissues/cells**
- Class III: TGA (Transmissible Spongiform Encephalopathies) risk
- Class IIb: Non-TGA risk
- Examples: Surgical sutures, collagen implants

**Rule 17: Nanomaterials**
- Class III: High or medium potential for internal exposure
- Class IIb: Low potential for internal exposure
- Examples: Nanoparticle-coated implants

**Rule 18: Combined products**
- Class III: Integral medicinal substance
- Class IIb: Ancillary medicinal substance
- Examples: Drug-eluting stents, antibiotic bone cement

**Rule 19: Ionizing radiation**
- Class IIb: Diagnostic/therapeutic ionizing radiation
- Examples: CT scanners, radiotherapy equipment

**Rule 20: Active devices for disinfection/sterilization**
- Class IIa: Medical device disinfection
- Class IIb: Surgical instrument sterilization
- Examples: Autoclaves, UV sterilizers

**Rule 21: Software**
- Class I: Information management
- Class IIa: Diagnosis/monitoring (low risk)
- Class IIb: Diagnosis/monitoring (high risk)
- Class III: Direct impact on patient safety
- Examples: AI diagnostic software, decision support systems

**Rule 22: contraceptive/prevention of disease transmission**
- Class IIa: Contraception, prevention of STDs
- Examples: Condoms, IUDs

## Classification Flowchart

```
Is it a medical device?
├─ No → Not covered by MDR
└─ Yes → Is it invasive?
   ├─ No → Non-invasive (Rules 1-4)
   │  ├─ Active? → Rule 4
   │  └─ Non-active → Rule 1-3
   └─ Yes → Invasive
      ├─ Body orifice? → Rule 5
      ├─ Surgically invasive?
      │  ├─ Transient? → Rule 6
      │  ├─ Reusable? → Rule 8 (Class I)
      │  └─ Short/Long term → Rule 7
      ├─ Active therapeutic? → Rule 9
      ├─ Active diagnostic? → Rule 10
      └─ Special rules → Rule 11-22
```

## Quick Reference Table

| Device Type | Examples | Classification |
|-------------|----------|----------------|
| Reusable surgical instruments | Scalpels, forceps | Class I |
| Non-invasive active devices | Thermometers, BP monitors | Class IIa |
| Short-term invasive | Catheters, endotracheal tubes | Class IIa |
| Long-term invasive (non-critical) | Orthopedic implants | Class IIb |
| Long-term invasive (critical) | Pacemakers, heart valves | Class III |
| Software (high impact) | AI diagnosis, treatment control | Class IIb/III |
| Nanomaterials (internal exposure) | Nanoparticle implants | Class III |
| Human tissues/cells | Tissue-engineered products | Class III |
| Drug-device combination (integral) | Drug-eluting stents | Class III |

## References

- **MDR 2017/745**: Annex VIII, Chapter III
- **Classification Rules**: Rules 1-22
- **Guidelines**: MDCG 2021-2 (Classification consultation)
