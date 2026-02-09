# OAuth 2.0 Authentication Flow Module

## Overview

Google Workspace OAuth 2.0 authentication implementation for ARIA Phase 4.

## Prerequisites

### Google Cloud Project Setup

1. Create Google Cloud Project
2. Enable APIs:
   - Gmail API
   - Google Docs API
   - Google Sheets API
   - Google Calendar API

### OAuth 2.0 Client Configuration

**Application Type**: Desktop App
**Authorized Redirect URI**: `http://localhost:3000/callback`

### Required Scopes

```
https://www.googleapis.com/auth/gmail.readonly
https://www.googleapis.com/auth/gmail.send
https://www.googleapis.com/auth/documents
https://www.googleapis.com/auth/spreadsheets
https://www.googleapis.com/auth/calendar
```

## Authentication Flow

### Step 1: Authorization Code Request

```typescript
interface AuthConfig {
  clientId: string;
  clientSecret: string;
  redirectUri: string;
}

function generateAuthUrl(config: AuthConfig): string {
  const scopes = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/calendar',
  ];

  const params = new URLSearchParams({
    client_id: config.clientId,
    redirect_uri: config.redirectUri,
    response_type: 'code',
    scope: scopes.join(' '),
    access_type: 'offline',
    prompt: 'consent',
  });

  return `https://accounts.google.com/o/oauth2/v2/auth?${params}`;
}
```

### Step 2: Exchange Authorization Code for Tokens

```typescript
interface TokenResponse {
  access_token: string;
  refresh_token: string;
  expires_in: number;
  token_type: string;
}

async function exchangeCodeForTokens(
  config: AuthConfig,
  code: string
): Promise<TokenResponse> {
  const response = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      client_id: config.clientId,
      client_secret: config.clientSecret,
      code,
      grant_type: 'authorization_code',
      redirect_uri: config.redirectUri,
    }),
  });

  if (!response.ok) {
    throw new Error(`Token exchange failed: ${response.statusText}`);
  }

  return response.json();
}
```

### Step 3: Refresh Access Token

```typescript
async function refreshAccessToken(
  config: AuthConfig,
  refreshToken: string
): Promise<Omit<TokenResponse, 'refresh_token'>> {
  const response = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      client_id: config.clientId,
      client_secret: config.clientSecret,
      refresh_token: refreshToken,
      grant_type: 'refresh_token',
    }),
  });

  if (!response.ok) {
    throw new Error(`Token refresh failed: ${response.statusText}`);
  }

  return response.json();
}
```

## Token Management

### Storage Structure

```typescript
interface TokenStore {
  access_token: string;
  refresh_token: string;
  expires_at: number; // Unix timestamp
  token_type: string;
}
```

### Token Validation

```typescript
function isTokenValid(store: TokenStore): boolean {
  return store.expires_at > Date.now();
}

async function getValidAccessToken(
  config: AuthConfig,
  store: TokenStore
): Promise<string> {
  if (isTokenValid(store)) {
    return store.access_token;
  }

  // Refresh token
  const newTokens = await refreshAccessToken(config, store.refresh_token);

  // Update store
  store.access_token = newTokens.access_token;
  store.expires_at = Date.now() + newTokens.expires_in * 1000;

  return newTokens.access_token;
}
```

## Security Considerations

1. **Token Storage**: Store tokens securely (system keychain, encrypted file)
2. **HTTPS Required**: All OAuth communication over HTTPS
3. **Scope Minimization**: Request only necessary scopes
4. **Token Rotation**: Use refresh tokens, minimize access token exposure
5. **Audit Logging**: Log all authentication events

## Error Handling

| Error | Description | Resolution |
|-------|-------------|------------|
| `invalid_client` | Client ID/Secret mismatch | Verify Google Cloud credentials |
| `invalid_grant` | Authorization code expired | Restart OAuth flow |
| `access_denied` | User denied consent | Explain required permissions |
| `invalid_scope` | Invalid scope requested | Verify scope URLs |

## Testing

### Test Configuration

```typescript
const testConfig: AuthConfig = {
  clientId: process.env.GOOGLE_CLIENT_ID,
  clientSecret: process.env.GOOGLE_CLIENT_SECRET,
  redirectUri: 'http://localhost:3000/callback',
};
```

### Test Cases

1. **Authorization URL Generation**: Verify correct URL parameters
2. **Token Exchange**: Mock Google token endpoint
3. **Token Refresh**: Verify refresh token usage
4. **Token Validation**: Check expiration handling
5. **Error Handling**: Test all error scenarios
