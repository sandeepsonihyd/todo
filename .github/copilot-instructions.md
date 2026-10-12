# TodoApp – Repository Instructions

Project-specific rules live in `.github/instructions/`:
- [backend.instructions.md](instructions/backend.instructions.md) → `backend/**`
- [frontend.instructions.md](instructions/frontend.instructions.md) → `frontend/**`

This file holds rules that apply to the whole workspace.

## Stack
- **Backend:** Python, FastAPI 0.115, Pydantic 2, Uvicorn (`backend/requirements.txt`, pinned versions).
- **Frontend:** React 19, JavaScript (JSX), Vite, oxlint (`frontend/package.json`).
- **Persistence:** Repository abstraction; no database is assumed.
- **Docs:** Product/technical requirements in `docs/PRD.md` and `docs/TRD.md`.

## Conventions
- Make small, focused changes. Do not refactor unrelated code.
- Names are descriptive and in English. Prefer clarity over cleverness.
- Comment only where intent is non-obvious; never restate the code.
- The API contract is `/api/todos...` JSON. Backend schemas and frontend API calls must change together.
- Keep configuration (URLs, origins, prefixes) out of business logic.
- Commit messages: imperative, concise subject (<72 chars), body explains *why*.

## Architecture
```
frontend (React/Vite, :5173)  --HTTP/JSON-->  backend (FastAPI, :8000, /api)
```
- Backend is layered: `api/routers` → `services` → `repositories`, with `schemas` for I/O models and `core` for config.
- Frontend is layered: `components` → `api` (the only place that calls `fetch`), with shared `constants`.
- Dependencies point inward only; lower layers never import upper layers.
- Frontend and backend are independent deployables and never import each other's code.

## Do
- Read `docs/PRD.md` / `docs/TRD.md` before adding or changing features.
- Reuse existing modules, schemas and components before creating new ones.
- Validate all external input at the boundary (Pydantic on the server, form checks on the client).
- Handle and surface errors explicitly with meaningful messages and status codes.
- Update the README or docs when behaviour, endpoints, or setup steps change.
- Run the relevant checks before finishing: `npm run lint` and `npm run build` in `frontend/`; `pytest` in `backend/` once tests exist.
- Keep dependencies minimal; pin backend versions and justify any new dependency.

## Do NOT
- Do not introduce TypeScript, new frameworks, or a database unless explicitly asked.
- Do not hardcode secrets, tokens, or environment-specific values; use configuration.
- Do not log sensitive data or return stack traces to clients.
- Do not bypass layers (e.g. router → repository, component → `fetch`).
- Do not add Python lint/format/type-check tooling or frontend tests unless asked.
- Do not edit lockfiles or generated output by hand.
- Do not make breaking API changes without updating both sides and the docs.
