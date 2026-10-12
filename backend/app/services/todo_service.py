"""Business logic for todo operations."""

from app.repositories.todo_repository import TodoRepository
from app.schemas.todo import Todo, TodoCreate, TodoStatusUpdate, TodoUpdate


class TodoService:
    """Coordinate todo validation and persistence."""

    def __init__(self, repository: TodoRepository | None = None) -> None:
        """Initialize the service with a repository."""
        self.repository = repository or TodoRepository()

    def get_all_todos(self) -> list[Todo]:
        """Return all repository records as todo schemas."""
        todos = self.repository.get_all()
        return [Todo.model_validate(todo) for todo in todos]

    def create_todo(self, todo_data: TodoCreate) -> Todo:
        """Create a todo from validated request data."""
        todo = self.repository.create(
            title=todo_data.title,
            description=todo_data.description,
            category=todo_data.category.value,
        )
        return Todo.model_validate(todo)

    def update_todo(self, todo_id: str, todo_data: TodoUpdate) -> Todo | None:
        """Update a todo, or return None if it does not exist."""
        todo = self.repository.update(
            my_todo_id=todo_id,
            title=todo_data.title,
            description=todo_data.description,
            category=todo_data.category.value,
        )
        if todo is None:
            return None
        return Todo.model_validate(todo)

    def update_status(
        self,
        todo_id: str,
        status_data: TodoStatusUpdate,
    ) -> Todo | None:
        """Update a todo's completion status, or return None if missing."""
        todo = self.repository.update_status(
            my_todo_id=todo_id,
            is_completed=status_data.is_completed,
        )
        if todo is None:
            return None
        return Todo.model_validate(todo)

    def delete_todo(self, todo_id: str) -> bool:
        """Delete a todo and report whether it existed."""
        return self.repository.delete(todo_id)
