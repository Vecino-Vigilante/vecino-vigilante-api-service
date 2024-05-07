from app.application.repositories.complaint_repository import ComplaintRepository
from app.domain.models.complaint_model import ComplaintModel


class ComplaintsService:
    def __init__(self, complaint_repository: ComplaintRepository):
        self.complaint_repository = complaint_repository
        
    def create_complaint(self, complaint: ComplaintModel, base64_image: str | None = None) -> ComplaintModel:
        pass