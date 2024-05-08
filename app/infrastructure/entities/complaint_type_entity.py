from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.infrastructure.entities.complaint_entity import Complaint

class ComplaintType(SQLModel, table=True):
    __tablename__ = "complaint_type"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    complaints: list["Complaint"] = Relationship(back_populates="incident_type")