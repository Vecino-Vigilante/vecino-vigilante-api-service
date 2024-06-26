from app.domain.models.complaint_comment_model import ComplaintCommentModel
from app.infrastructure.dto.complaint_comment_dto import (
    ComplaintCommentCreateDTO,
    ComplaintCommentDTO,
)
from app.infrastructure.entities.complaint_comment_entity import Comment
from app.infrastructure.mappers.user_mappers import (
    map_user_entity_to_user_model,
    map_user_model_to_user_logged_dto,
)


def map_complaint_comment_model_to_complaint_comment_dto(
    complaint_comment_model: ComplaintCommentModel,
) -> ComplaintCommentDTO:
    return ComplaintCommentDTO(
        id=complaint_comment_model.id,
        incident_id=complaint_comment_model.incident_id,
        content=complaint_comment_model.content,
        date=complaint_comment_model.date,
        image_url=complaint_comment_model.image_url,
        user=map_user_model_to_user_logged_dto(complaint_comment_model.user),
    )


def map_complaint_comment_entity_to_complaint_comment_model(
    complaint_comment_entity: Comment,
) -> ComplaintCommentModel:
    return ComplaintCommentModel(
        id=complaint_comment_entity.id,
        incident_id=complaint_comment_entity.incident_id,
        user_id=complaint_comment_entity.user_id,
        content=complaint_comment_entity.content,
        date=complaint_comment_entity.date,
        image_url=complaint_comment_entity.image_url,
        user=map_user_entity_to_user_model(complaint_comment_entity.user),
    )


def map_complaint_comment_dto_to_complaint_comment_model(
    complaint_comment_dto: ComplaintCommentCreateDTO,
) -> ComplaintCommentModel:
    return ComplaintCommentModel(
        id=None,
        incident_id=complaint_comment_dto.incident_id,
        user_id=complaint_comment_dto.user_id,
        content=complaint_comment_dto.content,
        date=complaint_comment_dto.date,
    )


def map_complaint_comment_model_to_complaint_comment_entity(
    complaint_comment_model: ComplaintCommentModel,
) -> Comment:
    return Comment(
        id=complaint_comment_model.id,
        incident_id=complaint_comment_model.incident_id,
        user_id=complaint_comment_model.user_id,
        content=complaint_comment_model.content,
        date=complaint_comment_model.date,
        image_url=complaint_comment_model.image_url,
    )
