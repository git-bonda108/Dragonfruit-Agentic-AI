# How to test real ClickUp integration

You have two ways to use ClickUp with this project: **1) Demo app (backend REST API)** and **2) ClickUp MCP in Cursor (IDE)**.

---

## 1. Demo app — real ClickUp via backend (PR-4 & ED-3)

This is what “Run demo” uses when the backend is running and your API key is set.

### Step 1: Set your API key

- Open **`DRAGONFRUIT/.env`** (project root, one level above `demo-app`).
- Ensure you have:
  ```bash
  CLICKUP_API_KEY=pk_your_actual_token_here
  ```
  (or `CLICKUP_PERSONAL_TOKEN`). No quotes needed unless the value has spaces.
- Get your token from ClickUp: **Settings → Apps → API Token** (starts with `pk_`).

### Step 2: Start the backend

In a **second** terminal (keep the frontend running in the first):

```bash
cd /Users/macbook/Documents/DRAGONFRUIT/demo-app
pip install -r backend/requirements.txt   # first time only
npm run backend
```

You should see:
```text
Uvicorn running on http://127.0.0.1:8000
```

The backend loads `.env` from **`DRAGONFRUIT/.env`** automatically.

### Step 3: Start the frontend (if not already)

In the **first** terminal:

```bash
cd /Users/macbook/Documents/DRAGONFRUIT/demo-app
npm run dev
```

Open **http://localhost:3000** in your browser.

### Step 4: Test real ClickUp in the app

1. Go to **Pipeline** → choose a **phase** (e.g. Pre-Production) → open a **role** that has **PR-4** or **ED-3** (e.g. Producer for PR-4, or the role that has ED-3).
2. Click the **PR-4** or **ED-3** opportunity tile.
3. Click **“Run demo”**.
4. **With backend + key configured:**
   - **PR-4:** You should see **“Live (MCP)”** (or “Live (API)”) and a real task created in your ClickUp workspace. The backend uses the first list it finds (team → space → folder/list). You’ll get an **“Open task →”** link.
   - **ED-3:** You should see **“Live (MCP)”** and suggested assignees from real tasks in that list.
5. **If the backend is not running or the key is missing:** You’ll see **“Mock”** and sample output only.

### Optional: Check backend health

```bash
curl http://localhost:8000/health
```

Response should include `"clickup_configured": true` when your key is loaded.

---

## 2. ClickUp MCP in Cursor (IDE)

You already have **ClickUp MCP** connected in Cursor. Use it for ad‑hoc testing and to see the same workspace the demo uses.

### What you can do in Cursor

- **List your workspace:** Ask the AI to call **`clickup_get_workspace_hierarchy`** (or use the MCP tool). You’ll see spaces and lists; use a **list ID** for create_task.
- **Create a task:** Ask to run **`clickup_create_task`** with:
  - `name`: e.g. `"Test from Cursor"`
  - `list_id`: from the hierarchy (e.g. `901613898970` for “Project 1”).
- **Get a task:** Use **`clickup_get_task`** with a `task_id` (e.g. from the create response).

### Quick test in Cursor

1. Ask: *“Call ClickUp get workspace hierarchy and show me the first list id.”*
2. Then: *“Create a ClickUp task in that list with name ‘Cursor MCP test’.”*
3. You should get back a `task_id` and `task_url`; open the URL to see the task in ClickUp.

---

## Summary

| Where        | How to test real ClickUp |
|-------------|---------------------------|
| **Demo app** | 1) Put `CLICKUP_API_KEY` in `DRAGONFRUIT/.env`. 2) Run `npm run backend` in demo-app. 3) Run `npm run dev`. 4) Open PR-4 or ED-3 and click **Run demo**. Look for **Live (MCP)** and the task link. |
| **Cursor IDE** | Use ClickUp MCP tools: `clickup_get_workspace_hierarchy`, `clickup_create_task`, `clickup_get_task`. Same workspace as your token. |

The **demo app backend** uses the **ClickUp REST API** (not the MCP server) because the app runs in the browser and cannot call Cursor’s MCP process. Same token, same workspace; MCP is for IDE use, REST API for the app.
