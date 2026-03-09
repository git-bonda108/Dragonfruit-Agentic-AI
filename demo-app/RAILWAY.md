# Deploy this app on Railway

1. **Set Root Directory to `demo-app`**
   - In your Railway project → **Settings** → **Service** (or "Source").
   - Set **Root Directory** to: `demo-app`
   - Save. Redeploy.

2. **Build & start (automatic)**
   - **Build:** `npm ci` then `npm run build` (Nixpacks uses `nixpacks.toml`).
   - **Start:** `npm start` (serves `dist/` on `$PORT`).

3. **Env vars (optional)**
   - For the backend API (ClickUp, OpenAI), add a separate Railway service for `demo-app/backend` and set `CLICKUP_API_KEY`, `OPENAI_API_KEY` there. The frontend here works without them (mock data).

If you deployed from **repo root** (no root directory set), Railpack fails because the app and `package.json` live in `demo-app/`. Setting Root Directory to `demo-app` fixes it.
