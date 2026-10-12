---
applyTo: "backend/**"
---

# Backend (FastAPI) Instructions

## Stack
- Python, FastAPI, Pydantic v2, Uvicorn.
- Entry point `backend/app/main.py`; run with `uvicorn app.main:app --reload` from `backend/`.
- Testing: `pytest` with FastAPI `TestClient` (add `pytest`/`httpx` to dev requirements when first used).

## Conventions
- Follow PEP 8; 4-space indent; `snake_case` for functions/variables, `PascalCase` for classes.
- Add type hints to all function signatures, including return types.
- Use Pydantic v2 APIs (`model_validate`, `model_dump`, `field_validator`), not v1 equivalents.
- Schema names describe purpose: `TodoCreate`, `TodoUpdate`, `TodoRead`.
- Routers are declared with `APIRouter(prefix="/api/<resource>", tags=[...])`.
- Always set `response_model` and explicit `status_code` on endpoints.
- Use `async def` only when the body awaits; otherwise plain `def`.
- Settings come from `app/core/config.py`.

## Architecture
```
app/
  api/routers/   HTTP only: parse, call service, map errors to HTTPException
  services/      business rules; no FastAPI imports
  repositories/  data access behind a small interface; swappable storage
  schemas/       Pydantic request/response models
  core/          config
```
- Routers depend on services; services depend on repositories. Never the reverse.
- Inject services and repositories via FastAPI `Depends` or constructor arguments rather than module globals, so they can be replaced in tests.
- Services raise domain errors; routers translate them to HTTP status codes (404, 409, 422).
- Storage is abstracted by the repository; do not leak storage details into services or routers.

## Do
- Put each new resource in its own router, service, repository and schema modules.
- Keep routers thin: no business logic or data access.
- Return consistent error bodies via `HTTPException(detail=...)`.
- Restrict CORS origins to the configured frontend origin.
- Write `pytest` tests for services (pure logic) and routers (via `TestClient`) for new behaviour.
- Use `pathlib`, f-strings, and context managers.

## Do NOT
- Do not access repositories from routers or import `fastapi` in services/repositories.
- Do not return internal objects; always return schemas.
- Do not use mutable default arguments or global mutable state beyond the repository instance.
- Do not use `allow_origins=["*"]` with credentials.
- Do not swallow exceptions (`except: pass`) or print for logging; use the `logging` module.
- Do not add Python linters/formatters/type-checker configuration unless asked.
- Do not add scratch or unrelated modules (e.g. `mymath.py`) to the app package.
