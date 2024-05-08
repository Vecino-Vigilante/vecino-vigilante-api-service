from abc import ABC, abstractmethod

from app.domain.models.complaint_comment_model import ComplaintCommentModel


class ComplaintCommentRepository(ABC):
    @abstractmethod
    def add_comment(self, complaint_comment: ComplaintCommentModel) -> ComplaintCommentModel:
        pass