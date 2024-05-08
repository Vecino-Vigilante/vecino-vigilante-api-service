from uuid import UUID
from fastapi import APIRouter, status

from app.application.services.complaint_comment_service import ComplaintCommentService
from app.infrastructure.dto.complaint_comment_dto import ComplaintCommentCreateDTO, ComplaintCommentDTO
from app.infrastructure.mappers.complaint_comment_mappers import map_complaint_comment_dto_to_complaint_comment_model, map_complaint_comment_model_to_complaint_comment_dto
from app.infrastructure.repositories.awss3_files_repository_impl import AWSS3FilesRepositoryImpl
from app.infrastructure.repositories.relational_db_complaint_comment_repository_impl import RelationalDBComplaintCommentRepositoryImpl

FOLDER_IN_BUCKET = 'complaints_comments'

complaint_comment_router = APIRouter()
complaint_comment_service = ComplaintCommentService(
    complaint_comment_repository=RelationalDBComplaintCommentRepositoryImpl(),
    files_repository=AWSS3FilesRepositoryImpl(FOLDER_IN_BUCKET),
)

@complaint_comment_router.post("", status_code=status.HTTP_201_CREATED)
def create_complaint_comment(comment: ComplaintCommentCreateDTO) -> ComplaintCommentDTO:
    new_comment = complaint_comment_service.add_complaint_comment(
        map_complaint_comment_dto_to_complaint_comment_model(comment),
        comment.resource
    )
    return map_complaint_comment_model_to_complaint_comment_dto(new_comment)

@complaint_comment_router.get("/{incident_id}")
def get_complaint_comments(incident_id: UUID) -> list[ComplaintCommentDTO]:
    return [
        map_complaint_comment_model_to_complaint_comment_dto(comment)
        for comment in complaint_comment_service.get_complaint_comments(incident_id)
    ]