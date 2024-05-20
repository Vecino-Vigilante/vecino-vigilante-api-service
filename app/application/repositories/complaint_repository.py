from abc import ABC, abstractmethod
from datetime import datetime
from uuid import UUID

from app.domain.models.complaint_model import ComplaintModel


class ComplaintRepository(ABC):
    @abstractmethod
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        pass

    @abstractmethod
    def get_complaints(
        self,
        start_date: datetime | None,
        end_date: datetime | None,
        type_id: UUID | None,
    ):
        pass

    @abstractmethod
    def get_complaint(self, incident_id: UUID) -> ComplaintModel:
        pass

    @abstractmethod
    def update_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        pass

    @abstractmethod
    def delete_complaint(self, incident_id: UUID):
        pass
