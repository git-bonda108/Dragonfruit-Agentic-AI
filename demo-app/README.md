# Dragonfruit — Agentic Pipeline Demo

**Gateway to the overall project.** This demo app shows the pipeline-first hierarchy: **Pipeline → Phase → Role → Opportunity**, with MCP integration, GIFs (agent trajectory), and dream allocation mapping.

## Run

**Easiest:** In Finder, go to `DRAGONFRUIT/demo-app` and **double‑click `START.command`**. A terminal will open, the server will start, and your browser should open to the app. Keep the terminal window open.

**Or from Terminal:**

```bash
cd /Users/macbook/Documents/DRAGONFRUIT/demo-app
npm install   # first time only
npm run dev
```

**Important:** Use the URL that opens in your browser (e.g. **http://localhost:3000**). Do not type only “localhost” — you must include the port, e.g. `http://localhost:3000`.

## Data

- **Public data:** `public/mock_data/` — all JSON is loaded from here (phase_roles, wishlist_tools, tool_io, tool_integration, tool_dream_mapping, time_allocations, ai_survey_summary, role_opportunities).
- **GIFs:** `public/gifs/` — HTML animations for agent trajectory; each opportunity links to a `gif_id` (e.g. `pr4_tool_use_react.html`).
- **Data manifest:** See `../mock_data/DATA_MANIFEST.md` for dependency order and file ↔ UI mapping.

## Batches

- **Batch 1–2 (done):** Data model (phase_roles, tool_io, tool_integration, tool_dream_mapping, role_opportunities) + scaffold, theme, pipeline view, GIFs in public.
- **Batch 3:** Phase detail → Roles → Opportunities (role cards with “Currently using”, dream one-liner, opportunity list).
- **Batch 4:** Opportunity detail (run demo, GIF iframe, input/output, integration, dream allocation).
- **Batch 5:** Trajectory page + polish.

## Stack

- Vite + React 18 + TypeScript
- React Router 6
- CSS variables (Dragonfruit palette), Plus Jakarta Sans
