# Deploy this app on Railway

1. **Set Root Directory to `demo-app`**
   - In your Railway project → **Settings** → **Service** (or "Source").
   - Set **Root Directory** to: `demo-app`
   - Save. Redeploy.

2. **Build & start (automatic)**
   - **Build:** `npm ci` then `npm run build` (Nixpacks uses `nixpacks.toml`).
   - **Start:** `npm start` → runs `serve -s dist -l tcp://0.0.0.0:${PORT:-3000}`. The app binds to **0.0.0.0** so Railway’s proxy can reach it. Railway sets **`PORT`**; no need to set it. Locally, port 3000 is used.

3. **Env vars (optional)**
   - For the backend API (ClickUp, OpenAI), add a separate Railway service for `demo-app/backend` and set `CLICKUP_API_KEY`, `OPENAI_API_KEY` there. The frontend here works without them (mock data).

If you deployed from **repo root** (no root directory set), Railpack fails because the app and `package.json` live in `demo-app/`. Setting Root Directory to `demo-app` fixes it.

---

**If the build still fails with `TS18047: 'rootEl' is possibly 'null'`:**

1. **Confirm Root Directory**  
   Railway → your service → **Settings** → **Root Directory** must be **`demo-app`** (not blank, not the repo root). Save.

2. **Clear build cache and redeploy**  
   In the same service, open **Deployments** (or **Settings**), find **Clear build cache** / **Redeploy** and run it so the next build uses the latest code and no cached `main.tsx`.

3. **Redeploy**  
   Trigger a new deploy (e.g. **Deploy** from the latest commit or push an empty commit). The fix is in `demo-app/src/main.tsx` (null check + `as HTMLElement`); the build must run from `demo-app/` and without stale cache.

---

**If you see "Application failed to respond"** (logs show "Accepting connections at http://localhost:8080" but the public URL doesn’t load):

- The app must listen on **0.0.0.0**, not only localhost, so Railway’s proxy can reach it. The start script uses `serve -s dist -l tcp://0.0.0.0:${PORT:-3000}` for this. Redeploy after pulling the latest code.
