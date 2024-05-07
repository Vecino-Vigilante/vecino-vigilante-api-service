from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.infrastructure.entities.complaint_entity import Complaint
    from app.infrastructure.entities.complaint_comment_entity import Comment


class User(SQLModel, table=True):
    id: UUID = Field(default=uuid4(), primary_key=True)
    name: str
    last_name: str
    email: str = Field(unique=True)
    password: str
    profile_image: str | None = Field(default=None)
    complaints: list["Complaint"] = Relationship(back_populates="user")
    comments: list["Comment"] = Relationship(back_populates="user")
