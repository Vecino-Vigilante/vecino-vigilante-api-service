from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.infrastructure.entities.complaint_entity import Complaint
    from app.infrastructure.entities.user_entity import User


class Comment(SQLModel, table=True):
    id: UUID = Field(default=uuid4(), primary_key=True)
    incident_id: UUID = Field(foreign_key="complaint.id")
    user_id: UUID = Field(foreign_key="user.id")
    content: str
    date: datetime
    image_url: str
    incident: "Complaint" = Relationship(back_populates="comments")
    user: "User" = Relationship(back_populates="comments")