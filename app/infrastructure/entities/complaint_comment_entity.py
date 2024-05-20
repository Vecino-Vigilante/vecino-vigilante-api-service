from datetime import datetime, timezone
from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.infrastructure.entities.complaint_entity import Complaint
    from app.infrastructure.entities.user_entity import User


class Comment(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    incident_id: UUID = Field(foreign_key="complaint.id")
    user_id: UUID = Field(foreign_key="user.id")
    content: str
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    image_url: str | None = Field(default=None)
    incident: "Complaint" = Relationship(back_populates="comments")
    user: "User" = Relationship(back_populates="comments")
