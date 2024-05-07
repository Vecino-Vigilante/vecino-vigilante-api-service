from app.domain.models.complaint_comment_model import ComplaintCommentModel
from app.infrastructure.dto.complaint_comment_dto import ComplaintCommentDTO
from app.infrastructure.mappers.user_mappers import map_user_model_to_user_logged_dto


def map_complaint_comment_model_to_complaint_comment_dto(complaint_comment_model: ComplaintCommentModel) -> ComplaintCommentDTO:
    return ComplaintCommentDTO(
        id=complaint_comment_model.id,
        incident_id=complaint_comment_model.incident_id,
        content=complaint_comment_model.content,
        date=complaint_comment_model.date,
        image_url=complaint_comment_model.image_url,
        user=map_user_model_to_user_logged_dto(complaint_comment_model.user),
    )