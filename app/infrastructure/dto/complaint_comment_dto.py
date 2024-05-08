from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

from app.infrastructure.dto.authenticated_user_dto import AuthenticatedUserDTO



class ComplaintCommentDTO(BaseModel):
    id: UUID
    incident_id: UUID
    content: str
    date: datetime
    image_url: str | None = None
    user: AuthenticatedUserDTO

class ComplaintCommentCreateDTO(BaseModel):
    incident_id: UUID
    user_id: UUID
    content: str
    date: datetime | None = None
    resource: str | None = None
    