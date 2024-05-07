from sqlmodel import Session, select

from app.application.repositories.user_repository import UserRepository
from app.domain.models.user_model import UserModel
from app.infrastructure.configs.sql_database import db_engine
from app.infrastructure.entities.user_entity import User
from app.infrastructure.mappers.user_mappers import (
    map_user_entity_to_user_model,
    map_user_model_to_user_entity,
)


class RelationalDBUserRepositoryImpl(UserRepository):
    def get_user_by_email(self, email: str) -> UserModel | None:
        with Session(db_engine) as session:
            user_entity = session.exec(select(User).where(User.email == email)).first()

            if user_entity:
                return map_user_entity_to_user_model(user_entity)

    def save_user(self, user: UserModel) -> UserModel:
        with Session(db_engine) as session:
            user_entity = None

            if user.id:
                user_entity = session.exec(select(User).where(User.id == user.id)).one()

                user_entity.email = user.email
                user_entity.last_name = user.last_name
                user_entity.name = user.name
                user_entity.password = user.password
            else:
                user_entity = map_user_model_to_user_entity(user)

            session.add(user_entity)
            session.commit()
            session.refresh(user_entity)

            return map_user_entity_to_user_model(user_entity)
