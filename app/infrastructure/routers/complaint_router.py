
from fastapi import APIRouter, status

from app.application.services.complaint_service import ComplaintsService
from app.infrastructure.repositories.relational_db_complaint_repository_impl import RelationalDBComplaintRepositoryImpl


complaint_router = APIRouter()
complaint_service = ComplaintsService(
    complaint_repository=RelationalDBComplaintRepositoryImpl()
)

@complaint_router.post("", status_code=status.HTTP_201_CREATED)
def create_complaint():
    return complaint_service.create_complaint()