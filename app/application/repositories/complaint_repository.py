from abc import ABC, abstractmethod

from app.domain.models.complaint_model import ComplaintModel


class ComplaintRepository(ABC):
    @abstractmethod
    def add_complaint(self, complaint: ComplaintModel) -> ComplaintModel:
        pass