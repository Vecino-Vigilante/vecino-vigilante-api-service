from datetime import datetime
from uuid import UUID

from app.domain.models.user_model import UserModel


class ComplaintCommentModel:
    def __init__(
        self,
        id: UUID | None,
        incident_id: UUID,
        user_id: UUID,
        content: str,
        date: datetime,
        image_url: str | None = None,
        user: UserModel | None = None
    ):
        self.id = id
        self.incident_id = incident_id
        self.user_id = user_id
        self.content = content
        self.date = date
        self.image_url = image_url
        self.user = user
