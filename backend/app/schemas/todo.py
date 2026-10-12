"""Pydantic schemas for todo requests and responses."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class CategoryEnum(str, Enum):
    official = "official"
    personal = "personal"
    general = "general"


class TodoBase(BaseModel):
    """Shared todo fields."""

    title: str = Field(..., min_length=1)
    description: str | None = None
    category: CategoryEnum = CategoryEnum.general

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str | None) -> str:
        """Reject blank titles and strip surrounding whitespace."""
        if value is None or value.strip() == "":
            raise ValueError("Title is required")
        return value.strip()


class TodoCreate(TodoBase):
    """Payload for creating a todo."""

    pass


class TodoUpdate(TodoBase):
    """Payload for updating a todo."""

    pass


class TodoStatusUpdate(BaseModel):
    """Payload for toggling completion state."""

    is_completed: bool


class Todo(TodoBase):
    """Todo returned by the API."""

    id: str
    date_created: datetime
    is_completed: bool = False

    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
    }
