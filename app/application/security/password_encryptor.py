class PasswordEncryptor:
    @staticmethod
    def get_password_hash(password: str) -> str:
        raise NotImplementedError(
            "Method get_password_hash hasn't been implemented yet."
        )

    @staticmethod
    def verify_password_hash(password: str, hashed_password: str) -> bool:
        raise NotImplementedError(
            "Method verify_password_hash hasn't been implemented yet."
        )
