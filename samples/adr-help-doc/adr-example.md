# ADR 004: Migrating Client Authentication to Short-Lived JSON Web Tokens (JWT)

## Status
Accepted

## Context
Our fictional customer portal application currently authenticates API clients using static, long-lived API tokens. These tokens are stored in the database and validated on every request. 
However, this presents security risks:
1. If a database is compromised, all active client tokens are leaked.
2. Invalidation of compromised tokens requires active database writes and database lookups on every single API request, increasing latency.

We need a more secure, decentralized, and stateless authentication mechanism that reduces database hits.

## Decision
We will migrate our client authentication scheme from static strings to short-lived JSON Web Tokens (JWTs). 

1. **Token Generation**: Clients will request a JWT by passing their credentials (Client ID and Client Secret) to the `/oauth/token` exchange endpoint.
2. **Lifetime**: The generated JWT will have an expiration time (`exp`) of 60 minutes.
3. **Validation**: Microservices will validate JWTs statelessly using the public key signature of our Identity Provider, removing the need for database lookups on standard API calls.
4. **Refresh**: Clients will use a rotating refresh token to obtain a new JWT without storing primary credentials in memory.

## Consequences
- **Security**: Compromised JWTs are only valid for a maximum of 60 minutes.
- **Latency**: Validation is CPU-bound rather than I/O-bound, saving database lookups on every request.
- **Complexity**: Clients must now handle token expiration and automatic refresh cycles.
