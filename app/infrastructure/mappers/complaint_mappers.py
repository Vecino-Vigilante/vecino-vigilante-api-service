from app.domain.models.complaint_model import ComplaintModel
from app.infrastructure.dto.complaint_dto import ComplaintDTO, ComplaintDetailDTO, ComplaintRequestDTO
from app.infrastructure.mappers.complaint_comment_mappers import map_complaint_comment_model_to_complaint_comment_dto
from app.infrastructure.mappers.marker_mappers import map_marker_model_to_marker_dto, map_marker_req_dto_to_marker_model
from app.infrastructure.mappers.user_mappers import map_user_model_to_user_logged_dto


def map_complaint_req_dto_to_complaint_model(complaint_request_dto: ComplaintRequestDTO) -> ComplaintModel:
    return ComplaintModel(
        id=None,
        type_id=complaint_request_dto.type_id,
        user_id=complaint_request_dto.user_id,
        description=complaint_request_dto.description,
        date=complaint_request_dto.date,
        location=map_marker_req_dto_to_marker_model(complaint_request_dto.location),
    )
    
def map_complaint_model_to_complaint_dto(complaint_model: ComplaintModel) -> ComplaintDTO:
    return ComplaintDTO(
        id=complaint_model.id,
        type=complaint_model.type,
        description=complaint_model.description,
        date=complaint_model.date,
        image_url=complaint_model.image_url,
        user=map_user_model_to_user_logged_dto(complaint_model.user),
        location=map_marker_model_to_marker_dto(complaint_model.location),
    )
    
def map_complaint_model_to_complaint_detail_dto(complaint_model: ComplaintModel) -> ComplaintDTO:
    return ComplaintDetailDTO(
        id=complaint_model.id,
        type=complaint_model.type,
        description=complaint_model.description,
        date=complaint_model.date,
        image_url=complaint_model.image_url,
        user=map_user_model_to_user_logged_dto(complaint_model.user),
        location=map_marker_model_to_marker_dto(complaint_model.location),
        comments=[
            map_complaint_comment_model_to_complaint_comment_dto(comment)
            for comment in complaint_model.comments
        ]
    )