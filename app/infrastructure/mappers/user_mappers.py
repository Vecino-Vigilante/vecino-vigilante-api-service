from app.domain.models.user_model import UserModel
from app.infrastructure.dto.authenticated_user_dto import AuthenticatedUserDTO
from app.infrastructure.entities.user_entity import User


def map_user_entity_to_user_model(user_entity: User) -> UserModel:
    return UserModel(
        email=user_entity.email,
        id=user_entity.id,
        last_name=user_entity.last_name,
        name=user_entity.name,
        password=user_entity.password,
    )


def map_user_model_to_user_entity(user_model: UserModel) -> User:
    return User(
        email=user_model.email,
        id=user_model.id,
        last_name=user_model.last_name,
        name=user_model.name,
        password=user_model.password,
    )


def map_user_model_to_user_logged_dto(user_model: UserModel) -> AuthenticatedUserDTO:
    return AuthenticatedUserDTO(
        id=user_model.id,
        email=user_model.email,
        last_name=user_model.last_name,
        name=user_model.name,
    )
