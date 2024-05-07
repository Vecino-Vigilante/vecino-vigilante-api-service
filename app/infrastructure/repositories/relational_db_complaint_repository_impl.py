from app.application.repositories.complaint_repository import ComplaintRepository
from app.domain.models.complaint_model import ComplaintModel


class RelationalDBComplaintRepositoryImpl(ComplaintRepository):
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        pass