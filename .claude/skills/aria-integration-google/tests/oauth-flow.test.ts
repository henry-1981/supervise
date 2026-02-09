/**
 * OAuth 2.0 Flow Tests for Google Workspace Integration
 *
 * These tests verify the OAuth 2.0 authentication flow implementation
 * for the ARIA Google Workspace integration skill.
 *
 * Test Categories:
 * 1. Authorization URL Generation
 * 2. Token Exchange
 * 3. Token Refresh
 * 4. Token Validation
 * 5. Error Handling
 */

import { describe, it, expect, beforeEach, jest } from '@jest/globals';

describe('OAuth 2.0 Flow', () => {
  const mockConfig = {
    clientId: 'test-client-id.apps.googleusercontent.com',
    clientSecret: 'test-client-secret',
    redirectUri: 'http://localhost:3000/callback'
  };

  describe('generateAuthUrl', () => {
    it('should generate valid authorization URL', () => {
      const url = generateAuthUrl(mockConfig);

      expect(url).toContain('https://accounts.google.com/o/oauth2/v2/auth');
      expect(url).toContain(`client_id=${mockConfig.clientId}`);
      expect(url).toContain(`redirect_uri=${encodeURIComponent(mockConfig.redirectUri)}`);
      expect(url).toContain('response_type=code');
      expect(url).toContain('access_type=offline');
      expect(url).toContain('prompt=consent');
    });

    it('should include all required scopes', () => {
      const url = generateAuthUrl(mockConfig);

      expect(url).toContain('https://www.googleapis.com/auth/gmail.readonly');
      expect(url).toContain('https://www.googleapis.com/auth/gmail.send');
      expect(url).toContain('https://www.googleapis.com/auth/documents');
      expect(url).toContain('https://www.googleapis.com/auth/spreadsheets');
      expect(url).toContain('https://www.googleapis.com/auth/calendar');
    });
  });

  describe('exchangeCodeForTokens', () => {
    beforeEach(() => {
      // Mock fetch for token exchange
      global.fetch = jest.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            access_token: 'test-access-token',
            refresh_token: 'test-refresh-token',
            expires_in: 3600,
            token_type: 'Bearer'
          })
        })
      ) as jest.Mock;
    });

    it('should exchange authorization code for tokens', async () => {
      const mockCode = 'test-authorization-code';
      const tokens = await exchangeCodeForTokens(mockConfig, mockCode);

      expect(tokens.access_token).toBe('test-access-token');
      expect(tokens.refresh_token).toBe('test-refresh-token');
      expect(tokens.expires_in).toBe(3600);
      expect(tokens.token_type).toBe('Bearer');
    });

    it('should throw error on invalid authorization code', async () => {
      (global.fetch as jest.Mock).mockImplementationOnce(() =>
        Promise.resolve({
          ok: false,
          statusText: 'invalid_grant'
        })
      );

      await expect(
        exchangeCodeForTokens(mockConfig, 'invalid-code')
      ).rejects.toThrow('Token exchange failed: invalid_grant');
    });
  });

  describe('refreshAccessToken', () => {
    beforeEach(() => {
      global.fetch = jest.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            access_token: 'new-access-token',
            expires_in: 3600,
            token_type: 'Bearer'
          })
        })
      ) as jest.Mock;
    });

    it('should refresh access token using refresh token', async () => {
      const mockRefreshToken = 'test-refresh-token';
      const tokens = await refreshAccessToken(mockConfig, mockRefreshToken);

      expect(tokens.access_token).toBe('new-access-token');
      expect(tokens.expires_in).toBe(3600);
      expect(tokens.token_type).toBe('Bearer');
      // Refresh token should NOT be returned in refresh response
      expect(tokens).not.toHaveProperty('refresh_token');
    });

    it('should throw error on invalid refresh token', async () => {
      (global.fetch as jest.Mock).mockImplementationOnce(() =>
        Promise.resolve({
          ok: false,
          statusText: 'invalid_grant'
        })
      );

      await expect(
        refreshAccessToken(mockConfig, 'invalid-refresh-token')
      ).rejects.toThrow('Token refresh failed: invalid_grant');
    });
  });

  describe('isTokenValid', () => {
    it('should return true for valid token', () => {
      const validStore = {
        access_token: 'test-token',
        refresh_token: 'test-refresh',
        expires_at: Date.now() + 3600 * 1000, // 1 hour from now
        token_type: 'Bearer'
      };

      expect(isTokenValid(validStore)).toBe(true);
    });

    it('should return false for expired token', () => {
      const expiredStore = {
        access_token: 'test-token',
        refresh_token: 'test-refresh',
        expires_at: Date.now() - 1000, // 1 second ago
        token_type: 'Bearer'
      };

      expect(isTokenValid(expiredStore)).toBe(false);
    });
  });

  describe('getValidAccessToken', () => {
    it('should return existing access token if valid', async () => {
      const validStore = {
        access_token: 'existing-token',
        refresh_token: 'test-refresh',
        expires_at: Date.now() + 3600 * 1000,
        token_type: 'Bearer'
      };

      const token = await getValidAccessToken(mockConfig, validStore);
      expect(token).toBe('existing-token');
    });

    it('should refresh token if expired', async () => {
      const expiredStore = {
        access_token: 'expired-token',
        refresh_token: 'test-refresh',
        expires_at: Date.now() - 1000,
        token_type: 'Bearer'
      };

      global.fetch = jest.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve({
            access_token: 'new-token',
            expires_in: 3600,
            token_type: 'Bearer'
          })
        })
      ) as jest.Mock;

      const token = await getValidAccessToken(mockConfig, expiredStore);
      expect(token).toBe('new-token');
      expect(expiredStore.access_token).toBe('new-token');
      expect(expiredStore.expires_at).toBeGreaterThan(Date.now());
    });
  });

  describe('Error Scenarios', () => {
    it('should handle invalid_client error', async () => {
      (global.fetch as jest.Mock).mockImplementationOnce(() =>
        Promise.resolve({
          ok: false,
          json: () => Promise.resolve({
            error: 'invalid_client'
          })
        })
      );

      await expect(
        exchangeCodeForTokens(mockConfig, 'code')
      ).rejects.toThrow();
    });

    it('should handle access_denied error', async () => {
      (global.fetch as jest.Mock).mockImplementationOnce(() =>
        Promise.resolve({
          ok: false,
          json: () => Promise.resolve({
            error: 'access_denied'
          })
        })
      );

      await expect(
        exchangeCodeForTokens(mockConfig, 'code')
      ).rejects.toThrow();
    });

    it('should handle network errors', async () => {
      (global.fetch as jest.Mock).mockImplementationOnce(() =>
        Promise.reject(new Error('Network error'))
      );

      await expect(
        exchangeCodeForTokens(mockConfig, 'code')
      ).rejects.toThrow('Network error');
    });
  });
});

// Helper functions for testing (implementation would be in actual module)

interface AuthConfig {
  clientId: string;
  clientSecret: string;
  redirectUri: string;
}

interface TokenResponse {
  access_token: string;
  refresh_token: string;
  expires_in: number;
  token_type: string;
}

interface TokenStore {
  access_token: string;
  refresh_token: string;
  expires_at: number;
  token_type: string;
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

  const newTokens = await refreshAccessToken(config, store.refresh_token);
  store.access_token = newTokens.access_token;
  store.expires_at = Date.now() + newTokens.expires_in * 1000;

  return newTokens.access_token;
}
