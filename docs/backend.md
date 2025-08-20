# Backend API

## Health
- `GET /health` → `{"status":"ok"}`

## Ponds
- `POST /ponds`
  - Body: `{ "name": "Pond A1", "location": "Site West" }`
  - Returns: `{ id, name, location, created_at }`
- `GET /ponds`
  - Returns: `[{ id, name, location, created_at }, ...]`

> Note: In the MVP the store is in-memory and resets when the server sleeps/restarts. We will replace it with Supabase Postgres in the next step.
