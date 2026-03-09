# ClickUp MCP — Verification (IDE)

ClickUp MCP is connected to this IDE (Cursor). The following was tested and verified.

## Tests run

1. **`clickup_get_workspace_hierarchy`**  
   - **Arguments:** `max_depth: 2`, `limit: 10`  
   - **Result:** Success. Returned workspace tree with spaces and lists (e.g. Team Space → Project 1, Project 2, Get Started with ClickUp).  
   - **Conclusion:** MCP is authenticated and can read your ClickUp workspace.

2. **`clickup_create_task`**  
   - **Arguments:** `name: "Dragonfruit demo verification"`, `list_id: "901613898970"` (Project 1), `description: "Created via Cursor ClickUp MCP test"`  
   - **Result:** Success. Returned `task_id: "86d280pcy"`, `task_url: "https://app.clickup.com/t/86d280pcy"`.  
   - **Conclusion:** Create-task flow works end-to-end via MCP.

## Using ClickUp MCP in the IDE

- **Workspace hierarchy:** Use `clickup_get_workspace_hierarchy` to see spaces and lists and resolve list IDs.
- **Create task:** Use `clickup_create_task` with `name` and `list_id` (and optional `description`, `assignees`, `due_date`, etc.).
- **Other tools:** The ClickUp MCP exposes more tools (e.g. `clickup_get_task`, `clickup_update_task`, `clickup_get_task_comments`). Use the MCP tool list in Cursor to discover and call them.

## Demo app vs IDE MCP

- **In Cursor:** You use the ClickUp MCP directly (as above). No extra setup.
- **In the demo app (browser):** The backend uses the **ClickUp REST API** with `CLICKUP_API_KEY` from `.env` for PR-4 and ED-3. The same workspace is used; the app cannot call the IDE’s MCP process. For a single “real ClickUp” path, the backend is wired to the REST API and is ready when the key is set.

## MCP synthesized data

Mock and demo data for the app are loaded from **`MCP SYNTHESIZED DATA`**:

- `clickup_workspace.json` — workspace structure (Dragonfruit Media, Mango/Lemon pods, lists).  
  Served by backend at **`GET /api/clickup/workspace`** when using mock data.
- `clickup_create_task_response.json` — PR-4 create-task response.  
  Used by backend for PR-4 when no API key or when API is unavailable.
- `clickup_assign_editor_response.json` — ED-3 assignee suggestion response.  
  Used by backend for ED-3 mock.
- `clickup_editor_capacity.json`, `clickup_tasks_mango_batch14.json`, `clickup_timeline_calculator_response.json` — available for richer mock or future endpoints.  
  Served by backend at **`GET /api/clickup/synthesized/{name}`** (e.g. `clickup_editor_capacity`).

All of the above keep mock data aligned with the MCP synthesized folder and make one real ClickUp path (REST API in the app + MCP in the IDE) ready.
