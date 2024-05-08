from datetime import datetime
from uuid import UUID
from fastapi import APIRouter, status

from app.application.services.complaint_service import ComplaintsService
from app.infrastructure.dto.complaint_dto import ComplaintRequestDTO
from app.infrastructure.mappers.complaint_mappers import (
    map_complaint_model_to_complaint_dto,
    map_complaint_req_dto_to_complaint_model,
)
from app.infrastructure.repositories.awss3_files_repository_impl import (
    AWSS3FilesRepositoryImpl,
)
from app.infrastructure.repositories.relational_db_complaint_repository_impl import (
    RelationalDBComplaintRepositoryImpl,
)


complaint_router = APIRouter()
complaint_service = ComplaintsService(
    complaint_repository=RelationalDBComplaintRepositoryImpl(),
    files_repository=AWSS3FilesRepositoryImpl(),
)


@complaint_router.post("", status_code=status.HTTP_201_CREATED)
def create_complaint(complaint: ComplaintRequestDTO):
    new_complaint = complaint_service.create_complaint(
        map_complaint_req_dto_to_complaint_model(complaint), complaint.resource
    )
    return map_complaint_model_to_complaint_dto(new_complaint)


@complaint_router.get("")
def get_complaints(
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    type_id: UUID | None = None,
):
    return [
        map_complaint_model_to_complaint_dto(complaint)
        for complaint in complaint_service.get_complaints(start_date, end_date, type_id)
    ]
