from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.models.complaint_comment_model import ComplaintCommentModel


class ComplaintCommentRepository(ABC):
    @abstractmethod
    def add_comment(
        self, complaint_comment: ComplaintCommentModel
    ) -> ComplaintCommentModel:
        pass

    @abstractmethod
    def get_complaint_comments(self, incident_id: UUID) -> list[ComplaintCommentModel]:
        pass

    @abstractmethod
    def get_comment(self, comment_id: UUID) -> ComplaintCommentModel:
        pass

    @abstractmethod
    def update_comment(
        self, complaint_comment: ComplaintCommentModel
    ) -> ComplaintCommentModel:
        pass

    @abstractmethod
    def delete_comment(self, comment_id: UUID):
        pass
