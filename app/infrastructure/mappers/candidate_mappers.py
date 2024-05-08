from pydantic import SecretStr
from app.domain.models.candidate_model import CandidateModel
from app.infrastructure.dto.candidate_dto import CandidateDTO


def map_candidate_dto_to_candidate_model(candidate_dto: CandidateDTO) -> CandidateModel:
    return CandidateModel(
        email=candidate_dto.email,
        last_name=candidate_dto.last_name,
        name=candidate_dto.name,
        password=candidate_dto.password.get_secret_value(),
    )


def map_candidate_model_to_candidate_dto(
    candidate_model: CandidateModel,
) -> CandidateDTO:
    return CandidateDTO(
        email=candidate_model.email,
        last_name=candidate_model.last_name,
        name=candidate_model.name,
        password=SecretStr(candidate_model.password),
    )
