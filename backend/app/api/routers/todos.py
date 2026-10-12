"""HTTP routes for todo management."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.todo import Todo, TodoCreate, TodoStatusUpdate, TodoUpdate
from app.services.todo_service import TodoService

router = APIRouter(prefix="/api/todos", tags=["todos"])
service = TodoService()


@router.get("", response_model=list[Todo])
def get_todos() -> list[Todo]:
    """Return all todos."""
    return service.get_all_todos()


@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate) -> Todo:
    """Create and return a todo."""
    return service.create_todo(todo)


@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: str, todo: TodoUpdate) -> Todo:
    """Update a todo, returning 404 if it does not exist."""
    updated_todo = service.update_todo(todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return updated_todo


@router.patch("/{todo_id}/status", response_model=Todo)
def update_todo_status(todo_id: str, todo: TodoStatusUpdate) -> Todo:
    """Update a todo's completion status."""
    updated_todo = service.update_status(todo_id, todo)
    if updated_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return updated_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str) -> None:
    """Delete a todo, returning 404 if it does not exist."""
    deleted = service.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return None
