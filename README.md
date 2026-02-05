# Cowork Supervisor

> Strategic orchestrator that coordinates multiple Claude Code plugins to solve complex tasks

## Overview

Cowork Supervisor is a Claude Code plugin that acts as an intelligent orchestrator. Instead of learning how to use each plugin individually (Finance, Legal, Marketing, Data, etc.), you describe your task in natural language and the Supervisor:

1. **Clarifies** your intent through targeted questions
2. **Discovers** available plugins and their capabilities
3. **Plans** the execution strategy
4. **Orchestrates** multiple plugins in parallel/sequential execution
5. **Aggregates** results into a coherent response

## Installation

### Standalone Installation (Recommended)

1. **Clone the plugin**:

```bash
git clone https://github.com/henry-1981/supervise.git \
  ~/.claude/plugins/local/cowork-supervisor
```

2. **Register in `~/.claude/plugins/installed_plugins.json`**:

```json
{
  "plugins": {
    "cowork-supervisor@local": [{
      "scope": "user",
      "installPath": "~/.claude/plugins/local/cowork-supervisor",
      "version": "1.0.0",
      "installedAt": "2026-02-05T00:00:00Z",
      "lastUpdated": "2026-02-05T00:00:00Z"
    }]
  }
}
```

> Note: If the file already has other plugins, add the `cowork-supervisor@local` entry to the existing `plugins` object.

3. **Enable in `~/.claude/settings.json`**:

```json
{
  "enabledPlugins": {
    "cowork-supervisor@local": true
  }
}
```

> Note: Add to the existing `enabledPlugins` object if other plugins are already enabled.

4. **Restart Claude Code**

### Via Marketplace (Alternative)

If you have `team-attention-plugins` marketplace installed:

```bash
git clone https://github.com/team-attention/plugins-for-claude-natives.git \
  ~/.claude/plugins/marketplaces/team-attention-plugins
```

Then enable `cowork-supervisor@team-attention-plugins` in settings.json

## Quick Start

```
/supervise "Analyze competitor TechCorp's financial health and IP portfolio"
```

The Supervisor will:
1. Ask clarifying questions (which competitor? what aspects? timeframe?)
2. Discover available plugins (Finance, Legal detected)
3. Present an execution plan for your approval
4. Execute plugins in parallel where possible
5. Aggregate results into a comprehensive analysis

## How It Works

```
Your Task Description
         |
         v
  [Intent Clarifier]
         |  Asks: What exactly do you need?
         |  Asks: Which domains are involved?
         v
  [Capability Discoverer]
         |  Scans: What plugins are installed?
         |  Maps: Which plugins can help?
         v
  [Supervisor Planner]
         |  Creates: Execution plan
         |  You: Approve or modify
         v
  [Orchestra]
         |  Executes: Parallel when possible
         |  Handles: Errors and fallbacks
         v
  [Aggregator]
         |  Combines: Results from all plugins
         |  Resolves: Conflicts between sources
         v
  Final Response with Sources
```

## Usage Examples

### Basic: Single Domain

```
/supervise "Create a marketing campaign for our new product"
```

### Cross-Domain: Multiple Plugins

```
/supervise "Analyze acquisition target: financial health, legal risks, and market position"
```

### Complex: Multi-Phase Workflow

```
/supervise "Quarterly business review: sales performance, customer feedback, and competitive landscape"
```

## Supported Plugins

The Supervisor can coordinate any installed Claude Code plugin:

| Domain | Example Plugins |
|--------|----------------|
| Finance | Budget analysis, Financial reports, Forecasting |
| Legal | Contract review, IP analysis, Compliance check |
| Marketing | Campaign planning, Market research, Brand analysis |
| Sales | Pipeline analysis, Territory planning, Forecasting |
| Data | Data connectors, Analytics, ETL |
| Customer Support | Ticket analysis, Satisfaction tracking |
| Product | Roadmap planning, Feature analysis |

## Project Structure

```
cowork-supervisor/
├── .claude-plugin/
│   ├── plugin.json        # Plugin manifest
│   └── capabilities.yaml  # Capability declaration
├── agents/
│   ├── supervisor.md      # Main orchestrator
│   ├── intent-clarifier.md
│   ├── capability-discoverer.md
│   ├── supervisor-planner.md
│   ├── orchestra.md
│   └── aggregator.md
├── skills/
│   └── cowork-supervisor/
│       └── SKILL.md
├── commands/
│   └── supervise.md
├── README.md
├── LICENSE
└── CHANGELOG.md
```

## Configuration

No configuration required. The Supervisor automatically:
- Detects installed plugins via `~/.claude/plugins/installed_plugins.json`
- Scans marketplace directories for available capabilities
- Adapts to your plugin ecosystem

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for [Claude Code](https://claude.ai/claude-code)
- Inspired by multi-agent orchestration patterns
- Part of the [Team Attention](https://github.com/team-attention) plugin ecosystem
