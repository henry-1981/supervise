# MCP Integration Guide for ARIA Phase 2

Model Context Protocol (MCP) server integration guide for ARIA regulatory compliance system.

## Overview

ARIA (Active Risk Inspection and Assessment) system uses multiple MCP servers to extend agent capabilities. This document describes which agents use which MCP servers, how to load tools, and practical usage patterns.

## Available MCP Servers

### Context7 MCP

**Purpose**: Up-to-date library documentation and code examples

**Key Capabilities**:
- Library documentation lookup from official sources
- Code example retrieval
- API reference access
- Version-specific documentation

**Tools Available**:
- `mcp__context7__resolve-library-id`: Find library identifiers
- `mcp__context7__query-docs`: Query documentation content

**Configuration**:
```json
{
  "context7": {
    "command": "/bin/bash",
    "args": ["-l", "-c", "exec npx -y @upstash/context7-mcp@latest"]
  }
}
```

**Use Cases**:
- Looking up regulatory framework documentation
- Finding latest API specifications
- Accessing code examples for implementation
- Retrieving best practices from official sources

### Sequential Thinking MCP

**Purpose**: Step-by-step reasoning for complex problem analysis

**Key Capabilities**:
- Complex problem decomposition
- Architecture decision analysis
- Technology trade-off evaluation
- Risk assessment methodology

**Tools Available**:
- `mcp__sequential-thinking__sequentialthinking`: Structured reasoning

**Configuration**:
```json
{
  "sequential-thinking": {
    "command": "/bin/bash",
    "args": ["-l", "-c", "exec npx -y @modelcontextprotocol/server-sequential-thinking"]
  }
}
```

**Use Cases**:
- Complex regulatory pathway analysis
- Multi-factor risk assessment
- Architecture decision documentation
- Root cause analysis for compliance issues

### Notion MCP

**Purpose**: Notion integration for documentation and knowledge management

**Key Capabilities**:
- Document creation and management
- Knowledge base synchronization
- Team collaboration support
- Version control integration

**Tools Available**:
- `mcp__claude_ai_Notion__notion-search`: Search Notion pages
- `mcp__claude_ai_Notion__notion-fetch`: Retrieve page content
- `mcp__claude_ai_Notion__notion-create-pages`: Create new pages
- `mcp__claude_ai_Notion__notion-update-page`: Update existing pages
- `mcp__claude_ai_Notion__notion-move-pages`: Move pages in hierarchy
- `mcp__claude_ai_Notion__notion-duplicate-page`: Duplicate pages
- `mcp__claude_ai_Notion__notion-create-database`: Create databases
- `mcp__claude_ai_Notion__notion-update-data-source`: Update data sources
- `mcp__claude_ai_Notion__notion-create-comment`: Add comments
- `mcp__claude_ai_Notion__notion-get-comments`: Retrieve comments
- `mcp__claude_ai_Notion__notion-get-teams`: Get team information
- `mcp__claude_ai_Notion__notion-get-users`: Get user information

**Configuration**:
```json
{
  "claude_ai_notion": {
    "command": "/bin/bash",
    "args": ["-l", "-c", "exec npx -y @modelcontextprotocol/server-notion"]
  }
}
```

**Use Cases**:
- Regulatory document management
- Compliance tracking databases
- Team knowledge base synchronization
- Audit trail documentation

## Configuration

### .mcp.json Setup

The MCP servers are configured in the `.mcp.json` file in the project root:

```json
{
  "$schema": "https://raw.githubusercontent.com/anthropics/claude-code/main/.mcp.schema.json",
  "mcpServers": {
    "context7": {
      "$comment": "Up-to-date documentation and code examples via Context7",
      "command": "/bin/bash",
      "args": ["-l", "-c", "exec npx -y @upstash/context7-mcp@latest"]
    },
    "sequential-thinking": {
      "$comment": "Step-by-step reasoning for complex problems",
      "command": "/bin/bash",
      "args": ["-l", "-c", "exec npx -y @modelcontextprotocol/server-sequential-thinking"]
    },
    "claude_ai_notion": {
      "$comment": "Notion integration for documentation and knowledge management",
      "command": "/bin/bash",
      "args": ["-l", "-c", "exec npx -y @modelcontextprotocol/server-notion"]
    }
  },
  "staggeredStartup": {
    "enabled": true,
    "delayMs": 500,
    "connectionTimeout": 15000
  }
}
```

### Environment Variables

Some MCP servers require additional authentication:

**Notion MCP Authentication**:
```bash
export NOTION_API_KEY="your_notion_integration_token"
export NOTION_DATABASE_ID="your_database_id"
```

**Context7 MCP**: No authentication required (public version)

**Sequential Thinking MCP**: No authentication required (public version)

### Connection Settings

The staggered startup configuration helps prevent connection issues:

```json
{
  "staggeredStartup": {
    "enabled": true,
    "delayMs": 500,
    "connectionTimeout": 15000
  }
}
```

- **enabled**: Stagger MCP server startup to reduce load
- **delayMs**: Delay between server starts (500ms recommended)
- **connectionTimeout**: Maximum time to wait for connection (15 seconds)

## Usage Patterns

### Tool Loading Protocol

MCP tools use deferred loading and must be explicitly loaded before use:

**Step 1: Use ToolSearch to discover and load tools**
```
ToolSearch("context7 docs")
```

**Step 2: Call the loaded tool directly**
```
mcp__context7__resolve-library-id({ libraryName: "react" })
```

### Tool Naming Convention

MCP tools follow a consistent naming pattern:

```
mcp__{server_name}__{tool_name}
```

Examples:
- `mcp__context7__resolve-library-id`
- `mcp__sequential-thinking__sequentialthinking`
- `mcp__claude_ai_Notion__notion-search`

### Best Practices

1. **Always ToolSearch first**: MCP tools must be loaded before use
2. **Use specific queries**: Narrow search queries for faster loading
3. **Handle errors gracefully**: MCP servers may be unavailable
4. **Cache results**: Store frequently accessed documentation
5. **Limit token usage**: Avoid redundant MCP calls

## Agent-MCP Mapping

### ARIA Expert Agents

| Agent | Context7 | Sequential Thinking | Notion |
|-------|----------|-------------------|--------|
| expert-researcher | ✅ | ✅ | ❌ |
| expert-writer | ✅ | ❌ | ❌ |
| expert-analyst | ❌ | ✅ | ❌ |
| expert-architect | ❌ | ✅ | ❌ |
| expert-reviewer | ✅ | ❌ | ❌ |

### MoAI Manager Agents

| Agent | Context7 | Sequential Thinking | Notion |
|-------|----------|-------------------|--------|
| manager-spec | ✅ | ❌ | ❌ |
| manager-docs | ❌ | ❌ | ✅ |
| manager-quality | ✅ | ❌ | ❌ |

### Agent Responsibilities

**expert-researcher**: Uses Context7 for regulatory research and Sequential Thinking for complex analysis workflows

**expert-writer**: Uses Context7 to access latest documentation references and writing standards

**expert-analyst**: Uses Sequential Thinking for complex statistical analysis and risk assessment methodologies

**expert-architect**: Uses Sequential Thinking for architecture decisions and system design trade-offs

**expert-reviewer**: Uses Context7 to verify compliance with current regulatory standards

**manager-docs**: Uses Notion MCP for documentation synchronization and knowledge base management

**manager-spec**: Uses Context7 to access latest specification patterns and requirements standards

**manager-quality**: Uses Context7 to verify compliance with current quality standards and best practices

## Usage Examples

### Example 1: Regulatory Research with Context7

Research regulatory requirements using Context7:

```
// Step 1: Load Context7 tools
ToolSearch("context7 regulatory documentation")

// Step 2: Find regulatory framework library
const libraryId = await mcp__context7__resolve-library-id({
  libraryName: "FDA regulations",
  query: "21 CFR Part 820 quality system"
})

// Step 3: Query specific documentation
const docs = await mcp__context7__query-docs({
  libraryId: libraryId.id,
  query: "validation requirements",
  metadata: true
})
```

**Use Case**: Finding latest regulatory requirements for ARIA system compliance validation

### Example 2: Complex Analysis with Sequential Thinking

Perform step-by-step risk pathway analysis:

```
// Step 1: Load Sequential Thinking tools
ToolSearch("sequential thinking analysis")

// Step 2: Conduct structured analysis
const analysis = await mcp__sequential-thinking__sequentialthinking({
  thought: "Analyze ARIA inspection pathway for potential compliance risks",
  nextThoughtNeeded: true,
  thoughtNumber: 1,
  totalThoughts: 5
})

// Continue analysis for remaining steps...
```

**Use Case**: Breaking down complex regulatory compliance scenarios into manageable steps

### Example 3: Document Sync with Notion MCP

Synchronize compliance documentation to Notion knowledge base:

```
// Step 1: Load Notion tools
ToolSearch("notion documentation")

// Step 2: Search for existing page
const searchResult = await mcp__claude_ai_Notion__notion-search({
  query: "ARIA compliance procedures"
})

// Step 3: Create or update page
const page = await mcp__claude_ai_Notion__notion-create-pages({
  parentId: searchResult.parentId,
  title: "Updated Compliance Procedures",
  content: "# Compliance Procedures\n\nUpdated content..."
})
```

**Use Case**: Maintaining shared knowledge base for regulatory compliance procedures

### Example 4: Architecture Decision Analysis

Use Sequential Thinking for architecture trade-off analysis:

```
ToolSearch("sequential thinking")

const decision = await mcp__sequential-thinking__sequentialthinking({
  thought: "Evaluate microservices vs monolithic architecture for ARIA system",
  nextThoughtNeeded: true,
  thoughtNumber: 1,
  totalThoughts: 8,
  isRevision: false
})

// Continue through analysis steps:
// 2. List regulatory compliance requirements
// 3. Assess microservices compliance impact
// 4. Evaluate monolithic approach
// 5. Compare audit trail capabilities
// 6. Analyze validation complexity
// 7. Consider maintenance burden
// 8. Make recommendation
```

**Use Case**: Documenting architecture decisions with regulatory compliance considerations

## Troubleshooting

### Connection Issues

**Problem**: MCP server fails to connect

**Symptoms**:
- ToolSearch returns no results
- MCP tools unavailable after loading
- Connection timeout errors

**Solutions**:
1. Verify `.mcp.json` configuration
2. Check network connectivity
3. Increase `connectionTimeout` value
4. Restart Claude Code
5. Verify npx is available in PATH

**Configuration Fix**:
```json
{
  "staggeredStartup": {
    "connectionTimeout": 30000  // Increase from 15000
  }
}
```

### Authentication Failures

**Problem**: Notion MCP authentication fails

**Symptoms**:
- "Unauthorized" errors
- "Invalid API key" messages
- Failed page creation/update

**Solutions**:
1. Verify `NOTION_API_KEY` is set
2. Check integration token permissions
3. Ensure database access is granted
4. Regenerate integration token if needed

**Verification**:
```bash
echo $NOTION_API_KEY  # Should display your key
```

### Tool Loading Failures

**Problem**: MCP tools not available after ToolSearch

**Symptoms**:
- "Tool not found" errors
- ToolSearch succeeds but tools unavailable

**Solutions**:
1. Ensure ToolSearch completes before calling tools
2. Check MCP server is running
3. Verify tool name spelling
4. Reload MCP server by restarting Claude Code

**Correct Pattern**:
```
// Step 1: Load tools
ToolSearch("context7")

// Step 2: Wait for loading to complete

// Step 3: Use tools
mcp__context7__resolve-library-id({ libraryName: "react" })
```

### Fallback Mechanisms

When MCP servers are unavailable, the system provides fallback options:

**Context7 Fallback**:
- Use WebSearch for documentation
- Access cached local documentation
- Use official websites directly

**Sequential Thinking Fallback**:
- Break down problems manually
- Use standard reasoning patterns
- Document thought process explicitly

**Notion Fallback**:
- Use local file system for documents
- Generate markdown documentation
- Use alternative knowledge base systems

## Performance Optimization

### Token Budget Management

MCP operations consume tokens. Optimize usage:

1. **Batch queries**: Combine multiple requests when possible
2. **Cache results**: Store frequently accessed documentation
3. **Specific queries**: Use targeted search terms
4. **Limit scope**: Request only necessary information

### Connection Pooling

The staggered startup configuration enables efficient connection management:

```json
{
  "staggeredStartup": {
    "enabled": true,
    "delayMs": 500,
    "connectionTimeout": 15000
  }
}
```

- Reduces initial startup load
- Prevents connection conflicts
- Improves reliability

### Error Recovery

Implement robust error handling:

```
try {
  const result = await mcp__context7__resolve-library-id({
    libraryName: "regulations"
  })
} catch (error) {
  // Fallback to alternative documentation source
  const fallback = await WebSearch("regulatory requirements")
}
```

## Security Considerations

### API Key Management

- Never commit API keys to version control
- Use environment variables for sensitive credentials
- Rotate keys regularly
- Monitor access logs

### Data Privacy

- Be aware that MCP servers may process data externally
- Verify data retention policies
- Understand data transmission paths
- Review compliance requirements

### Access Control

- Limit MCP server permissions
- Use read-only access when possible
- Audit MCP server usage regularly
- Document access requirements

## Additional Resources

- [MCP Official Documentation](https://modelcontextprotocol.io/)
- [Claude Code MCP Integration Guide](https://github.com/anthropics/claude-code)
- [MoAI MCP Integration Rules](../.claude/rules/moai/core/mcp-integration.md)
- [ARIA System Documentation](./README.md)

---

**Version**: 1.0.0
**Last Updated**: 2026-02-09
**Maintained by**: MoAI ARIA Team
**Language**: English (Korean version also available)
