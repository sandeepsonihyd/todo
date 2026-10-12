---
applyTo: "frontend/**"
---

# Frontend (React + JavaScript) Instructions

## Stack
- React 19 function components, JavaScript/JSX (no TypeScript), Vite, oxlint.
- Commands from `frontend/`: `npm run dev`, `npm run lint`, `npm run build`.
- Dev server `http://localhost:5173`; API at `http://localhost:8000/api`.
- No frontend test framework is configured; do not add one unless asked.

## Conventions
- Components: `PascalCase.jsx`, one component per file, default export.
- Non-component modules: `camelCase.js` (e.g. `todoApi.js`); constants in `src/constants/`.
- Function components and hooks only; no class components.
- ES modules, `const` by default, no `var`, strict equality.
- Props are destructured in the signature; keep components small and focused.
- Use stable, unique `key` values (the todo id), never array indexes for dynamic lists.
- Styling stays consistent with existing CSS; follow the `frontend-design` skill for new UI work.
- Code must pass `npm run lint` with no warnings.

## Architecture
```
src/
  main.jsx        bootstrap
  App.jsx         top-level state and composition
  components/     presentational + interaction components
  api/            all HTTP calls (fetch wrappers)
  constants/      shared constants (e.g. categories)
```
- State lives in the lowest common ancestor; pass data down via props and events up via callbacks.
- Only `src/api/` calls `fetch`. Components consume its functions.
- API functions check `response.ok`, throw meaningful errors, and return parsed JSON.
- Derive values during render rather than duplicating them in state.

## Do
- Handle loading, empty, and error states for every async interaction.
- Keep the API base URL in one place; prefer a Vite env var (`import.meta.env.VITE_API_URL`) with a local default.
- Use semantic HTML, labels for inputs, and keyboard-accessible controls.
- Clean up effects (abort fetches, clear timers) and list dependencies correctly.
- Reuse shared constants instead of repeating literals such as category names.
- Keep payload shapes aligned with backend schemas.

## Do NOT
- Do not call `fetch` directly inside components.
- Do not mutate state or props; create new arrays/objects.
- Do not use `dangerouslySetInnerHTML` with user data.
- Do not store secrets in frontend code or env vars.
- Do not add TypeScript, state-management libraries, or UI frameworks without approval.
- Do not leave `console.log` or commented-out code.
- Do not disable lint rules to silence warnings; fix the cause.
