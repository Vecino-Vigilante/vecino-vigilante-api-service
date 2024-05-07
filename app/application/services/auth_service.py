from app.application.repositories.user_repository import UserRepository
from app.application.security.password_encryptor import PasswordEncryptor
from app.domain.exceptions.conflict_with_existing_resource_exception import (
    ConflictWithExistingResourceException,
)
from app.domain.exceptions.invalid_credentials_exception import (
    InvalidCredentialsException,
)
from app.domain.models.candidate_model import CandidateModel
from app.domain.models.user_model import UserModel


class AuthService:
    def __init__(
        self,
        password_encryptor: PasswordEncryptor,
        user_repository: UserRepository,
    ) -> None:
        self.password_encryptor = password_encryptor
        self.user_repository = user_repository

    def login(self, email: str, password: str) -> UserModel:
        user = self.user_repository.get_user_by_email(email)

        if not user or not self.password_encryptor.verify_password_hash(
            password, user.password
        ):
            raise InvalidCredentialsException

        return user

    def signup(self, candidate: CandidateModel) -> UserModel:
        if self.user_repository.get_user_by_email(candidate.email):
            raise ConflictWithExistingResourceException

        registered_user = self.user_repository.save_user(
            UserModel(
                id=None,
                email=candidate.email,
                last_name=candidate.last_name,
                name=candidate.name,
                password=self.password_encryptor.get_password_hash(candidate.password),
            )
        )

        return registered_user
