from uuid import UUID
from pydantic import BaseModel


class MarkerDTO(BaseModel):
    id: UUID
    incident_id: UUID
    latitude: float
    longitude: float
    direction: str


class MarkerRequestDTO(BaseModel):
    latitude: float
    longitude: float
    direction: str
