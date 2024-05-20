from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from app.infrastructure.dto.authenticated_user_dto import AuthenticatedUserDTO
from app.infrastructure.dto.complaint_comment_dto import ComplaintCommentDTO
from app.infrastructure.dto.marker_dto import MarkerDTO, MarkerRequestDTO


class TypeDTO(BaseModel):
    id: UUID
    name: str


class ComplaintDTO(BaseModel):
    id: UUID
    type: TypeDTO
    description: str
    date: datetime
    image_url: str | None = None
    user: AuthenticatedUserDTO
    location: MarkerDTO


class ComplaintDetailDTO(ComplaintDTO):
    comments: list[ComplaintCommentDTO] = []


class ComplaintRequestDTO(BaseModel):
    type_id: UUID
    user_id: UUID
    description: str
    date: datetime
    location: MarkerRequestDTO
    resource: str | None = None
