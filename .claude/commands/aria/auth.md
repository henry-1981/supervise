---
name: aria-auth
description: >
  ARIA OAuth authentication command for MCP server authentication setup. Handles OAuth 2.0 flows
  for Google Workspace (Gmail, Docs, Sheets, Calendar), Notion API, and Context7 MCP. Per SPEC-ARIA-004
  requirements including token management and automatic refresh.
license: Apache-2.0
compatibility: Designed for Claude Code
user-invocable: true
metadata:
  version: "2.1.0"
  category: "aria"
  status: "active"
  updated: "2026-02-09"
  tags: "aria, auth, oauth, google, notion, context7, token-management"
  argument-hint: "<service> <action> [options]"
---

# /aria auth Command

ARIA OAuth authentication management for MCP server integration (per SPEC-ARIA-004 S2.3).

## Usage

```bash
/aria auth google setup
/aria auth google status
/aria auth google refresh
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| service | string | Yes | Service to authenticate (google, notion, context7) |
| action | string | No | Action: setup, status, refresh, revoke |

## Google Workspace Authentication (SPEC-ARIA-004 S2.3)

### Setup OAuth 2.0

```bash
/aria auth google setup
```

**Behavior (per SPEC-ARIA-004 S2.3 OAuth 2.0 flow):**

1. **Google Cloud Project Configuration**
   - Check if `.mcp.json` exists
   - Prompt for Google Cloud Project credentials
   - Validate CLIENT_ID and CLIENT_SECRET format

2. **OAuth Consent Screen Setup**
   - Guide user through Google Cloud Console setup
   - List required scopes for Gmail, Docs, Sheets, Calendar
   - Configure redirect URI: `http://localhost:3000/callback`

3. **Authorization Flow (per SPEC-ARIA-004 S2.3)**
   ```
   1. User runs /aria auth google setup
   2. Google OAuth consent page displays
   3. User grants authorization (access_token, refresh_token obtained)
   4. Tokens stored securely (encrypted storage)
   5. API calls use access_token
   6. Token expiration triggers refresh_token for renewal
   ```

4. **Token Storage**
   - Store tokens securely in environment variables
   - Update `.mcp.json` with credentials
   - Validate token access with test API call

**Required Scopes (per SPEC-ARIA-004):**

```
https://www.googleapis.com/auth/gmail.readonly
https://www.googleapis.com/auth/gmail.send
https://www.googleapis.com/auth/documents
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/calendar
```

**Output:**

```markdown
## Google Workspace OAuth Setup Complete

✅ Authorization successful
✅ Tokens stored in environment variables
✅ MCP server configured

Configuration added to .mcp.json:
```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-google-workspace"],
      "env": {
        "GOOGLE_CLIENT_ID": "your_client_id.apps.googleusercontent.com",
        "GOOGLE_CLIENT_SECRET": "your_client_secret",
        "GOOGLE_REFRESH_TOKEN": "your_refresh_token"
      }
    }
  }
}
```

Next Steps:
1. Restart Claude Code to load MCP server
2. Test connection: /aria auth google status
```

### Check Authentication Status

```bash
/aria auth google status
```

**Behavior:**

1. Check if Google Workspace MCP server is configured
2. Verify environment variables are set
3. Test API access with a simple query
4. Report token expiration status

**Output:**

```markdown
## Google Workspace Authentication Status

✅ MCP Server Configured
✅ Access Token Valid (expires in 3500 seconds)
✅ Refresh Token Present

API Access Test:
- Gmail API: ✅ Working
- Docs API: ✅ Working
- Sheets API: ✅ Working
- Calendar API: ✅ Working

Token Details:
- Access Token Expires: 2026-02-09T12:00:00Z
- Refresh Token: Present
```

### Refresh Access Token

```bash
/aria auth google refresh
```

**Behavior:**

1. Use refresh token to obtain new access token
2. Update stored token
3. Validate new token with API call
4. Report new expiration time

**Output:**

```markdown
## Access Token Refreshed

✅ New access token obtained
✅ Token stored in environment
✅ API access validated

New Token Expires: 2026-02-09T13:00:00Z
```

### Revoke Authentication

```bash
/aria auth google revoke
```

**Behavior:**

1. Revoke Google OAuth tokens
2. Remove credentials from environment
3. Update `.mcp.json` to remove server config
4. Confirm revocation

**Output:**

```markdown
## Google Workspace Authentication Revoked

✅ Tokens revoked at Google
✅ Credentials removed from environment
✅ MCP server configuration removed

To re-authenticate, run: /aria auth google setup
```

## Environment Variables

### Required Variables

```bash
# Google Workspace OAuth
GOOGLE_CLIENT_ID="your_client_id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="your_client_secret"
GOOGLE_REDIRECT_URI="http://localhost:3000/callback"
GOOGLE_REFRESH_TOKEN="your_refresh_token"
```

### Storage Locations

**Linux/macOS:** `~/.bashrc` or `~/.zshrc`
**Windows:** Environment Variables in System Properties

## Error Handling

| Error | Description | Resolution |
|-------|-------------|------------|
| `invalid_client` | Invalid CLIENT_ID/SECRET | Verify Google Cloud credentials |
| `invalid_grant` | Authorization code expired | Restart OAuth flow |
| `access_denied` | User denied consent | Explain required permissions |
| `unauthorized` | Token expired | Run refresh command |
| `mcp_not_loaded` | MCP server not loaded | Restart Claude Code |

## Security Best Practices

1. **Never Commit Tokens**: Add `.env` to `.gitignore`
2. **Use Environment Variables**: Store credentials outside code
3. **Limit Scopes**: Request only necessary permissions
4. **Regular Refresh**: Refresh tokens before expiration
5. **Audit Access**: Monitor OAuth activity in Google Cloud Console

## Integration with ARIA Workflow

### Brief Phase

- Check authentication status before task planning
- Prompt for setup if not authenticated

### Execute Phase

- Use authenticated access for Google Workspace operations
- Handle token refresh automatically
- Report authentication issues to user

### Deliver Phase

- Verify authentication before final output
- Include authentication status in deliverable summary

## Notion Authentication

Similar flow for Notion MCP server:

```bash
/aria auth notion setup
/aria auth notion status
```

Required: `NOTION_API_KEY` and `NOTION_DATABASE_ID`

## Context7 Authentication

For Context7 MCP server:

```bash
/aria auth context7 setup
/aria auth context7 status
```

Required: `CONTEXT7_API_KEY`

---

**Version:** 2.1.0 (Phase 4 - SPEC-ARIA-004 Milestone 5)
**Last Updated:** 2026-02-09
**Language:** English
**Core Principle:** OAuth authentication management for MCP server integration
**Spec Compliance:** SPEC-ARIA-004 S2.3, SR-004
