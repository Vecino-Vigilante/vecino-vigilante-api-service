from uuid import UUID, uuid4
from app.application.repositories.complaint_comment_repository import (
    ComplaintCommentRepository,
)
from app.application.repositories.files_repository import FilesRepository
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.domain.models.complaint_comment_model import ComplaintCommentModel


class ComplaintCommentService:
    def __init__(
        self,
        complaint_comment_repository: ComplaintCommentRepository,
        files_repository: FilesRepository,
    ):
        self.complaint_comment_repository = complaint_comment_repository
        self.files_repository = files_repository

    def add_complaint_comment(
        self, complaint_comment: ComplaintCommentModel, base64_image: str | None = None
    ) -> ComplaintCommentModel:
        if base64_image:
            complaint_comment.id = uuid4()
            complaint_comment.image_url = self.files_repository.upload_base64(
                base64_image, str(complaint_comment.id).replace("-", "")
            )
        return self.complaint_comment_repository.add_comment(complaint_comment)

    def get_complaint_comments(self, incident_id: UUID) -> list[ComplaintCommentModel]:
        return self.complaint_comment_repository.get_complaint_comments(incident_id)

    def get_comment_by_id(self, comment_id: UUID) -> ComplaintCommentModel:
        comment = self.complaint_comment_repository.get_comment(comment_id)
        if not comment:
            raise ResourceNotFoundException
        return comment

    def update_complaint_comment(
        self, complaint_comment: ComplaintCommentModel, base64_image: str | None = None
    ) -> ComplaintCommentModel:
        if self.get_comment_by_id(complaint_comment.id):
            if base64_image:
                complaint_comment.image_url = self.files_repository.upload_base64(
                    base64_image, str(complaint_comment.id).replace("-", "")
                )
            return self.complaint_comment_repository.update_comment(complaint_comment)

    def delete_comment(self, comment_id: UUID):
        if self.get_comment_by_id(comment_id):
            self.complaint_comment_repository.delete_comment(comment_id)
