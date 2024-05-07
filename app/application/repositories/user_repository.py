from app.domain.models.user_model import UserModel


class UserRepository:
    def get_user_by_email(self, email: str) -> UserModel | None:
        raise NotImplementedError(
            "Method get_user_by_email hasn't been implemented yet."
        )

    def save_user(self, user: UserModel) -> UserModel:
        raise NotImplementedError("Method save_user hasn't been implemented yet.")
