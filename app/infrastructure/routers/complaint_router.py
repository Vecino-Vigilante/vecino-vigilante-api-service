from datetime import datetime
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status

from app.application.services.complaint_service import ComplaintsService
from app.domain.exceptions.resource_not_found_exception import ResourceNotFoundException
from app.infrastructure.dto.complaint_dto import (
    ComplaintDTO,
    ComplaintDetailDTO,
    ComplaintRequestDTO,
)
from app.infrastructure.mappers.complaint_mappers import (
    map_complaint_model_to_complaint_detail_dto,
    map_complaint_model_to_complaint_dto,
    map_complaint_req_dto_to_complaint_model,
)
from app.infrastructure.middleware.protect_route_middleware import (
    protect_route_middlware,
)
from app.infrastructure.repositories.awss3_files_repository_impl import (
    AWSS3FilesRepositoryImpl,
)
from app.infrastructure.repositories.relational_db_complaint_repository_impl import (
    RelationalDBComplaintRepositoryImpl,
)

FOLDER_IN_BUCKET = "complaints"

complaint_router = APIRouter(dependencies=[Depends(protect_route_middlware)])
complaint_service = ComplaintsService(
    complaint_repository=RelationalDBComplaintRepositoryImpl(),
    files_repository=AWSS3FilesRepositoryImpl(FOLDER_IN_BUCKET),
)


@complaint_router.post("", status_code=status.HTTP_201_CREATED)
def create_complaint(complaint: ComplaintRequestDTO) -> ComplaintDTO:
    new_complaint = complaint_service.create_complaint(
        map_complaint_req_dto_to_complaint_model(complaint), complaint.resource
    )
    return map_complaint_model_to_complaint_dto(new_complaint)


@complaint_router.get("")
def get_complaints(
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    type_id: UUID | None = None,
) -> list[ComplaintDTO]:
    return [
        map_complaint_model_to_complaint_dto(complaint)
        for complaint in complaint_service.get_complaints(start_date, end_date, type_id)
    ]


@complaint_router.get("/{incident_id}")
def get_complaint_by_id(incident_id: UUID) -> ComplaintDetailDTO:
    try:
        return map_complaint_model_to_complaint_detail_dto(
            complaint_service.get_complaint_by_id(incident_id)
        )
    except ResourceNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Complaint not found"
        )


@complaint_router.put("/{incident_id}")
def update_complaint(incident_id: UUID, complaint: ComplaintRequestDTO) -> ComplaintDTO:
    try:
        complaint_model = map_complaint_req_dto_to_complaint_model(complaint)
        complaint_model.id = incident_id
        return map_complaint_model_to_complaint_dto(
            complaint_service.update_complaint(complaint_model, complaint.resource)
        )
    except ResourceNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Complaint not found"
        )


@complaint_router.delete("/{incident_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_complaint(incident_id: UUID) -> None:
    try:
        complaint_service.delete_complaint(incident_id)
    except ResourceNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Complaint not found"
        )
