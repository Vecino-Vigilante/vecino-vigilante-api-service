from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from uuid import UUID, uuid4

if TYPE_CHECKING:
    from app.infrastructure.entities.user_entity import User

from app.infrastructure.entities.complaint_comment_entity import Comment
from app.infrastructure.entities.marker_entity import Marker
from app.infrastructure.entities.complaint_type_entity import ComplaintType

class Complaint(SQLModel, table=True):
    id: UUID = Field(default=uuid4(), primary_key=True)
    type_id: UUID = Field(foreign_key="complaint_type.id")
    user_id: UUID = Field(foreign_key="user.id")
    description: str
    date: datetime
    image_url: str
    incident_type: "ComplaintType" = Relationship(back_populates="complaints")
    user: "User" = Relationship(back_populates="complaints")
    marker: "Marker" = Relationship(back_populates="incident")
    comments: list["Comment"] = Relationship(back_populates="incident")