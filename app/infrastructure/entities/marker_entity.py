from typing import TYPE_CHECKING
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.infrastructure.entities.complaint_entity import Complaint

class Marker(SQLModel, table=True):
    marker_id: UUID = Field(default=uuid4(), primary_key=True)
    incident_id: UUID = Field(foreign_key="complaint.id")
    direction: str
    latitude: float
    longitude: float
    incident: "Complaint" = Relationship(back_populates="markers")