from datetime import datetime
from uuid import UUID, uuid4
from app.application.repositories.complaint_repository import ComplaintRepository
from app.application.repositories.files_repository import FilesRepository
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
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

    def get_complaints(
        self,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        type_id: UUID | None = None,
    ):
        return self.complaint_repository.get_complaints(start_date, end_date, type_id)

    def get_complaint_by_id(self, incident_id: UUID):
        complaint = self.complaint_repository.get_complaint(incident_id)
        if not complaint:
            raise ResourceNotFoundException
        return complaint
    
    def update_complaint(self, complaint: ComplaintModel, base64_image: str | None = None) -> ComplaintModel:
        if base64_image:
            complaint.image_url = self.files_repository.upload_base64(
                base64_image, str(complaint.id).replace("-", "")
            )
        if self.get_complaint_by_id(complaint.id):
            return self.complaint_repository.update_complaint(complaint)
        
    def delete_complaint(self, incident_id: UUID):
        if self.get_complaint_by_id(incident_id):
            self.complaint_repository.delete_complaint(incident_id)