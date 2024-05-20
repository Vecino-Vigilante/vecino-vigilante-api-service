from app.domain.models.complaint_model import ComplaintModel
from app.domain.models.complaint_type_model import ComplaintTypeModel
from app.infrastructure.dto.complaint_dto import (
    ComplaintDTO,
    ComplaintDetailDTO,
    ComplaintRequestDTO,
    TypeDTO,
)
from app.infrastructure.entities.complaint_entity import Complaint
from app.infrastructure.mappers.complaint_comment_mappers import (
    map_complaint_comment_model_to_complaint_comment_dto,
)
from app.infrastructure.mappers.marker_mappers import (
    map_marker_entity_to_marker_model,
    map_marker_model_to_marker_dto,
    map_marker_model_to_marker_entity,
    map_marker_req_dto_to_marker_model,
)
from app.infrastructure.mappers.user_mappers import (
    map_user_entity_to_user_model,
    map_user_model_to_user_logged_dto,
)


def map_complaint_req_dto_to_complaint_model(
    complaint_request_dto: ComplaintRequestDTO,
) -> ComplaintModel:
    return ComplaintModel(
        id=None,
        type_id=complaint_request_dto.type_id,
        user_id=complaint_request_dto.user_id,
        description=complaint_request_dto.description,
        date=complaint_request_dto.date,
        location=map_marker_req_dto_to_marker_model(complaint_request_dto.location),
    )


def map_complaint_model_to_complaint_entity(
    complaint_model: ComplaintModel,
) -> Complaint:
    return Complaint(
        id=complaint_model.id,
        type_id=complaint_model.type_id,
        user_id=complaint_model.user_id,
        description=complaint_model.description,
        date=complaint_model.date,
        image_url=complaint_model.image_url,
        marker=map_marker_model_to_marker_entity(complaint_model.location),
    )


def map_complaint_entity_to_complaint_model(
    complaint_entity: Complaint,
) -> ComplaintModel:
    return ComplaintModel(
        id=complaint_entity.id,
        type_id=complaint_entity.type_id,
        user_id=complaint_entity.user_id,
        description=complaint_entity.description,
        date=complaint_entity.date,
        image_url=complaint_entity.image_url,
        location=map_marker_entity_to_marker_model(complaint_entity.marker),
        type=ComplaintTypeModel(
            id=complaint_entity.incident_type.id,
            name=complaint_entity.incident_type.name,
        ),
        user=map_user_entity_to_user_model(complaint_entity.user),
    )


def map_complaint_model_to_complaint_dto(
    complaint_model: ComplaintModel,
) -> ComplaintDTO:
    return ComplaintDTO(
        id=complaint_model.id,
        type=TypeDTO(
            id=complaint_model.type.id,
            name=complaint_model.type.name,
        ),
        description=complaint_model.description,
        date=complaint_model.date,
        image_url=complaint_model.image_url,
        user=map_user_model_to_user_logged_dto(complaint_model.user),
        location=map_marker_model_to_marker_dto(complaint_model.location),
    )


def map_complaint_model_to_complaint_detail_dto(
    complaint_model: ComplaintModel,
) -> ComplaintDetailDTO:
    return ComplaintDetailDTO(
        id=complaint_model.id,
        type=TypeDTO(
            id=complaint_model.type.id,
            name=complaint_model.type.name,
        ),
        description=complaint_model.description,
        date=complaint_model.date,
        image_url=complaint_model.image_url,
        user=map_user_model_to_user_logged_dto(complaint_model.user),
        location=map_marker_model_to_marker_dto(complaint_model.location),
        comments=[
            map_complaint_comment_model_to_complaint_comment_dto(comment)
            for comment in complaint_model.comments
        ],
    )
