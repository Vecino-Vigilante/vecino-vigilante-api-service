from datetime import datetime
from uuid import UUID

from app.domain.models.complaint_comment_model import ComplaintCommentModel
from app.domain.models.complaint_type_model import ComplaintTypeModel
from app.domain.models.marker_model import MarkerModel
from app.domain.models.user_model import UserModel


class ComplaintModel:
    def __init__(
        self,
        id: UUID | None,
        type_id: UUID,
        user_id: UUID,
        description: str,
        date: datetime,
        image_url: str | None,
        location: MarkerModel,
        comments: list[ComplaintCommentModel] = [],
        type: ComplaintTypeModel | None = None,
        user: UserModel | None = None,
    ):
        self.id = id
        self.type_id = type_id
        self.user_id = user_id
        self.description = description
        self.date = date
        self.image_url = image_url
        self.location = location
        self.comments = comments
        self.type = type
        self.user = user
