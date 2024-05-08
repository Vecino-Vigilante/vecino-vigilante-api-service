from app.domain.models.marker_model import MarkerModel
from app.infrastructure.dto.marker_dto import MarkerDTO, MarkerRequestDTO
from app.infrastructure.entities.marker_entity import Marker


def map_marker_req_dto_to_marker_model(marker_request_dto: MarkerRequestDTO) -> MarkerModel:
    return MarkerModel(
        id=None,
        incident_id=None,
        latitude=marker_request_dto.latitude,
        longitude=marker_request_dto.longitude,
        direction=marker_request_dto.direction
    )
    
def map_marker_model_to_marker_entity(marker_model: MarkerModel) -> Marker:
    return Marker(
        latitude=marker_model.latitude,
        longitude=marker_model.longitude,
        direction=marker_model.direction
    )
    
def map_marker_entity_to_marker_model(marker_entity: Marker) -> MarkerModel:
    return MarkerModel(
        id=marker_entity.id,
        incident_id=marker_entity.incident_id,
        latitude=marker_entity.latitude,
        longitude=marker_entity.longitude,
        direction=marker_entity.direction
    )
    
def map_marker_model_to_marker_dto(marker_model: MarkerModel) -> MarkerDTO:
    return MarkerDTO(
        id=marker_model.id,
        incident_id=marker_model.incident_id,
        latitude=marker_model.latitude,
        longitude=marker_model.longitude,
        direction=marker_model.direction
    )