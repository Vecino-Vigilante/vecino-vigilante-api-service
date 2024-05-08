from uuid import uuid4
from app.application.repositories.complaint_repository import ComplaintRepository
from app.application.repositories.files_repository import FilesRepository
from app.domain.models.complaint_model import ComplaintModel


class ComplaintsService:
    def __init__(
        self,
        complaint_repository: ComplaintRepository,
        files_repository: FilesRepository,
    ):
        self.complaint_repository = complaint_repository
        self.files_repository = files_repository

    def create_complaint(
        self, complaint: ComplaintModel, base64_image: str | None = None
    ) -> ComplaintModel:
        if base64_image:
            complaint.id = uuid4()
            complaint.image_url = self.files_repository.upload_base64(
                base64_image, str(complaint.id).replace("-", "")
            )
        return self.complaint_repository.add_complaint(complaint)
