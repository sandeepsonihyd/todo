"""FastAPI application entry point for the Todo API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.todos import router as todos_router

app = FastAPI(title="Todo API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return the application health status."""
    return {"status": "ok"}
