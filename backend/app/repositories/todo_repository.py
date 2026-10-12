"""In-memory repository for todo records."""

from datetime import datetime, timezone


class TodoRepository:
    """Store and mutate todos in memory."""

    def __init__(self) -> None:
        """Initialize an empty in-memory todo collection."""
        self.todos = []

    def get_all(self) -> list[dict]:
        """Return all stored todo records."""
        return self.todos

    def get_by_id(self, my_todo_id: str) -> dict | None:
        """Return the todo with the given ID, if present."""
        for todo in self.todos:
            if todo["id"] == my_todo_id:
                return todo
        return None

    def create(self, title: str, description: str | None = None, category: str = "general") -> dict:
        """Create and store a todo record."""
        new_todo = {
            "id": str(len(self.todos) + 1),
            "title": title,
            "description": description,
            "category": category,
            "date_created": datetime.now(timezone.utc),
            "is_completed": False,
        }
        self.todos.append(new_todo)
        return new_todo

    def update(
        self,
        my_todo_id: str,
        title: str,
        description: str | None = None,
        category: str = "general",
    ) -> dict | None:
        """Update a stored todo, or return None if it does not exist."""
        todo = self.get_by_id(my_todo_id)
        if todo is None:
            return None

        todo["title"] = title
        todo["description"] = description
        todo["category"] = category
        return todo

    def update_status(self, my_todo_id: str, is_completed: bool) -> dict | None:
        """Update a todo's completion status, or return None if missing."""
        todo = self.get_by_id(my_todo_id)
        if todo is None:
            return None

        todo["is_completed"] = is_completed
        return todo

    def delete(self, my_todo_id: str) -> bool:
        """Delete a todo and report whether it existed."""
        todo = self.get_by_id(my_todo_id)
        if todo is None:
            return False

        self.todos = [item for item in self.todos if item["id"] != my_todo_id]
        return True
