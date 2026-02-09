# Library ID Mappings

Context7 library ID mappings for FDA 21 CFR 820, ISO 13485, EU MDR 2017/745, and related regulatory standards.

## Overview

Context7 MCP requires library IDs to resolve specific regulatory document collections. This module provides the complete mapping of library IDs to regulations, including query patterns and metadata for ARIA regulatory research automation.

## FDA Regulations

### FDA 21 CFR 820 - Quality System Regulation (QSR)

**Library ID**: `fda-21-cfr-part-820`

**Alternative IDs**:
- `fda-qsr`
- `21-cfr-820`
- `fda-quality-system-regulation`

**Query Patterns**:
```javascript
// Standard resolution
mcp__context7__resolve-library-id({
  query: "fda 21 cfr 820"
});

// Alternative patterns
mcp__context7__resolve-library-id({
  query: "fda qsr quality system regulation"
});

mcp__context7__resolve-library-id({
  query: "21 cfr part 820 medical device quality system"
});
```

**Metadata**:
- **Authority**: U.S. Food and Drug Administration (FDA)
- **Publication**: eCFR (electronic Code of Federal Regulations)
- **Last Updated**: Quarterly (January, April, July, October)
- **Language**: English
- **Format**: Structured regulation text

### FDA 21 CFR 820.30 - Design Controls

**Library ID**: `fda-21-cfr-820-design-controls`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "fda design controls 820.30"
});
```

### FDA 21 CFR 820.100 - Traceability

**Library ID**: `fda-21-cfr-820-traceability`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "fda traceability 820.100"
});
```

### FDA 510(k) Guidance Documents

**Library ID**: `fda-510k-guidance`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "fda 510(k) guidance documents"
});
```

### FDA PMA Requirements

**Library ID**: `fda-pma-requirements`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "fda premarket approval pma requirements"
});
```

## ISO Standards

### ISO 13485:2016 - Quality Management Systems

**Library ID**: `iso-13485`

**Alternative IDs**:
- `iso-13485-2016`
- `iso-medical-device-qms`

**Query Patterns**:
```javascript
// Standard resolution
mcp__context7__resolve-library-id({
  query: "iso 13485"
});

// Version-specific
mcp__context7__resolve-library-id({
  query: "iso 13485:2016"
});

// Descriptive
mcp__context7__resolve-library-id({
  query: "iso 13485 quality management systems medical devices"
});
```

**Metadata**:
- **Authority**: International Organization for Standardization (ISO)
- **Publication**: ISO Standard
- **Last Updated**: Annually (typically January)
- **Language**: English, French
- **Format**: Structured standard clauses

### ISO 14971:2019 - Risk Management

**Library ID**: `iso-14971`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "iso 14971 risk management medical devices"
});
```

**Metadata**:
- **Authority**: ISO
- **Current Version**: ISO 14971:2019
- **Related Standards**: ISO 13485, IEC 62304

### IEC 62304:2006 - Software Life Cycle Processes

**Library ID**: `iec-62304`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "iec 62304 software life cycle processes medical device software"
});
```

**Metadata**:
- **Authority**: International Electrotechnical Commission (IEC)
- **Current Version**: IEC 62304:2006 + AMD1:2010
- **Related Standards**: ISO 13485, ISO 14971

### ISO 14971:2019 - Risk Management (Cross-Reference)

**Library ID**: `iso-risk-management`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "iso risk management principles 14971"
});
```

## EU MDR Regulations

### EU MDR 2017/745 - Medical Device Regulation

**Library ID**: `eu-mdr-2017-745`

**Alternative IDs**:
- `eu-mdr`
- `medical-device-regulation-2017-745`
- `mdr-2017-745`

**Query Patterns**:
```javascript
// Standard resolution
mcp__context7__resolve-library-id({
  query: "eu mdr 2017/745"
});

// Abbreviated
mcp__context7__resolve-library-id({
  query: "eu mdr medical device regulation"
});

// Descriptive
mcp__context7__resolve-library-id({
  query: "regulation eu 2017/745 medical devices"
});
```

**Metadata**:
- **Authority**: European Commission
- **Publication**: Official Journal of the European Union
- **Last Updated**: As needed (implementing acts, delegated acts)
- **Language**: All EU official languages
- **Format**: Structured regulation with articles, annexes, chapters

### EU MDR Annex I - General Safety and Performance Requirements

**Library ID**: `eu-mdr-annex-i`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "eu mdr annex i general safety and performance requirements"
});
```

### EU MDR Annex IX - Conformity Assessment

**Library ID**: `eu-mdr-annex-ix`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "eu mdr annex ix conformity assessment procedures"
});
```

### EU MDR Annex XIV - Clinical Evaluation

**Library ID**: `eu-mdr-annex-xiv`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "eu mdr annex xiv clinical evaluation requirements"
});
```

## Korea MFDS Regulations

### Medical Device Act (Korea)

**Library ID**: `mfds-medical-device-act`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "korea medical device act mfds"
});
```

**Metadata**:
- **Authority**: Ministry of Food and Drug Safety (MFDS)
- **Language**: Korean, English
- **Last Updated**: As needed

### MFDS Notification - Technical Documentation

**Library ID**: `mfds-technical-docs`

**Query Patterns**:
```javascript
mcp__context7__resolve-library-id({
  query: "mfds technical documentation requirements notification"
});
```

## Library Resolution Algorithm

### Resolution Strategy

```javascript
async function resolveRegulationLibrary(regulationType, regulationName) {
  const queryPatterns = getQueryPatterns(regulationType);

  for (const pattern of queryPatterns) {
    try {
      const result = await mcp__context7__resolve-library-id({
        query: pattern.replace('{name}', regulationName)
      });

      if (result.libraryId) {
        return {
          libraryId: result.libraryId,
          queryUsed: pattern,
          alternatives: result.alternatives || []
        };
      }
    } catch (error) {
      continue; // Try next pattern
    }
  }

  throw new Error(`Unable to resolve library for ${regulationType}: ${regulationName}`);
}
```

### Query Pattern Selection

**FDA Regulations**:
1. "fda {regulation-name}" - Most specific
2. "{regulation-name} fda" - Alternative
3. "21 cfr {section-number}" - CFR format
4. "{title} medical device" - Descriptive

**ISO Standards**:
1. "iso {standard-number}:{year}" - Version-specific
2. "iso {standard-number}" - Standard format
3. "{standard-name} iso" - Descriptive

**EU MDR**:
1. "eu mdr {regulation-number}" - Official format
2. "eu {regulation-name}" - Abbreviated
3. "regulation {number} {title}" - Full format

## Library Metadata Structure

### Metadata Record

```javascript
{
  libraryId: "fda-21-cfr-part-820",
  regulationType: "FDA",
  regulationName: "21 CFR 820 - Quality System Regulation",
  authority: "U.S. Food and Drug Administration",
  publicationSource: "eCFR",
  currentVersion: "Current as of 2026-02-09",
  lastUpdateDate: "2026-01-01",
  updateSchedule: "quarterly",
  languages: ["en"],
  format: "structured-regulation",
  queryPatterns: [
    "fda 21 cfr 820",
    "fda qsr",
    "21 cfr part 820"
  ],
  relatedLibraries: [
    "fda-21-cfr-820-design-controls",
    "fda-21-cfr-820-traceability"
  ],
  citationFormat: "21 CFR §820.XX"
}
```

## Fallback and Error Handling

### Fallback Strategy

```javascript
async function resolveLibraryWithFallback(regulationType, regulationName) {
  try {
    // Primary resolution attempt
    const primary = await resolveRegulationLibrary(regulationType, regulationName);
    return primary;
  } catch (primaryError) {
    try {
      // Fallback to generic search
      const fallback = await genericContext7Search(regulationName);
      return fallback;
    } catch (fallbackError) {
      // Final fallback: use manual mapping
      const manual = lookupManualMapping(regulationType, regulationName);
      if (manual) {
        return manual;
      }
      throw new Error(`Unable to resolve library: ${regulationName}`);
    }
  }
}
```

### Manual Mapping Lookup

```javascript
const manualLibraryMappings = {
  'fda-21-cfr-820': {
    libraryId: 'fda-21-cfr-part-820',
    queryPatterns: ['fda 21 cfr 820', 'fda qsr']
  },
  'iso-13485': {
    libraryId: 'iso-13485',
    queryPatterns: ['iso 13485', 'iso 13485:2016']
  },
  'eu-mdr-2017-745': {
    libraryId: 'eu-mdr-2017-745',
    queryPatterns: ['eu mdr 2017/745', 'eu mdr']
  }
};
```

## Integration with ARIA Workflow

### Brief Phase Integration

```javascript
// During Brief phase, resolve libraries for identified regulations
async function briefPhaseLibraryResolution(regulations) {
  const libraryPromises = regulations.map(reg =>
    resolveRegulationLibrary(reg.type, reg.name)
  );

  const libraries = await Promise.all(libraryPromises);

  // Store resolved libraries for Execute phase
  return libraries.map(lib => ({
    regulationType: lib.regulationType,
    libraryId: lib.libraryId,
    queryUsed: lib.queryUsed
  }));
}
```

### Execute Phase Integration

```javascript
// During Execute phase, use resolved libraries for queries
async function executePhaseQuery(libraryId, topic) {
  const results = await mcp__context7__get-library-docs({
    libraryId: libraryId,
    query: topic
  });

  // Cache results for future use
  await cacheQueryResult(libraryId, topic, results);

  return results;
}
```

## Maintenance and Updates

### Library ID Updates

**Monthly Review**:
- Check for new regulation additions
- Verify existing library IDs are still valid
- Update metadata for changed regulations

**Quarterly Updates**:
- Align with FDA quarterly updates
- Update ISO standard versions
- Refresh EU MDR implementing acts

**Update Process**:
1. Query Context7 for latest library list
2. Compare with existing mappings
3. Identify new, changed, or deprecated libraries
4. Update manual mappings
5. Test query patterns
6. Update documentation

---

Last Updated: 2026-02-09
Maintained by: ARIA Development Team
