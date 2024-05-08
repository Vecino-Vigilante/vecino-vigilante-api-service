from abc import ABC, abstractmethod
from app.domain.models.user_model import UserModel


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> UserModel | None:
        pass

    @abstractmethod
    def save_user(self, user: UserModel) -> UserModel:
        pass
