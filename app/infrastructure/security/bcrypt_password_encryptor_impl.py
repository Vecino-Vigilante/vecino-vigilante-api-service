from passlib.context import CryptContext

from app.application.security.password_encryptor import PasswordEncryptor


class BcryptPasswordEncryptorImpl(PasswordEncryptor):
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def get_password_hash(password: str) -> str:
        return BcryptPasswordEncryptorImpl.password_context.hash(password)

    @staticmethod
    def verify_password_hash(password: str, hashed_password: str) -> bool:
        return BcryptPasswordEncryptorImpl.password_context.verify(
            password, hashed_password
        )
