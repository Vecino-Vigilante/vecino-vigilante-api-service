import unittest
from unittest.mock import Mock, patch
from app.application.repositories.user_repository import UserRepository
from app.application.security.password_encryptor import PasswordEncryptor
from app.domain.exceptions.conflict_with_existing_resource_exception import ConflictWithExistingResourceException
from app.domain.exceptions.invalid_credentials_exception import InvalidCredentialsException
from app.domain.models.candidate_model import CandidateModel
from app.domain.models.user_model import UserModel
from app.application.services.auth_service import AuthService


class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.password_encryptor = Mock(spec=PasswordEncryptor)
        self.user_repository = Mock(spec=UserRepository)
        self.auth_service = AuthService(
            password_encryptor=self.password_encryptor,
            user_repository=self.user_repository,
        )

    def test_login_success(self):
        email = "user@example.com"
        password = "password"
        hashed_password = "hashed_password"
        user = UserModel(
            id=1, 
            email=email, 
            last_name="Herrera", 
            name="Carlos", 
            password=hashed_password)

        self.user_repository.get_user_by_email.return_value = user
        self.password_encryptor.verify_password_hash.return_value = True

        log_data = self.auth_service.login(email, password)

        self.user_repository.get_user_by_email.assert_called_once_with(email)
        self.password_encryptor.verify_password_hash.assert_called_once_with(password, user.password)
        self.assertEqual(log_data, user)

    def test_login_invalid_credentials(self):
        email = "user@example.com"
        password = "password"

        self.user_repository.get_user_by_email.return_value = None

        with self.assertRaises(InvalidCredentialsException):
            self.auth_service.login(email, password)

        self.user_repository.get_user_by_email.assert_called_once_with(email)
        self.password_encryptor.verify_password_hash.assert_not_called()

    def test_login_wrong_password(self):
        email = "user@example.com"
        password = "password"
        hashed_password = "hashed_password"
        user = UserModel(
            id=1, 
            email=email, 
            last_name="Herrera", 
            name="Carlos", 
            password=hashed_password)

        self.user_repository.get_user_by_email.return_value = user
        self.password_encryptor.verify_password_hash.return_value = False

        with self.assertRaises(InvalidCredentialsException):
            self.auth_service.login(email, password)

        self.user_repository.get_user_by_email.assert_called_once_with(email)
        self.password_encryptor.verify_password_hash.assert_called_once_with(password, user.password)

    
    def test_signup_success(self):
        email = "newuser@example.com"
        candidate = CandidateModel(
            email=email, 
            last_name="Herrera", 
            name="Carlos", 
            password="password")
        hashed_password = "hashed_password"
        user = UserModel(
            id=1, 
            email=email, 
            last_name="Herrera", 
            name="Carlos", 
            password=hashed_password)

        self.user_repository.get_user_by_email.return_value = None
        self.password_encryptor.get_password_hash.return_value = hashed_password
        self.user_repository.save_user.return_value = user

        sign_data = self.auth_service.signup(candidate)

        self.user_repository.get_user_by_email.assert_called_once_with(candidate.email)
        self.password_encryptor.get_password_hash.assert_called_once_with(candidate.password)
        self.user_repository.save_user.assert_called_once()
        self.assertEqual(sign_data, user)

    def test_signup_conflict_with_existing_resource(self):
        email = "user@example.com"
        candidate = CandidateModel(
            email=email, 
            last_name="Herrera", 
            name="Carlos", 
            password="password")
        existing_user = UserModel(
            id=1, 
            email=email, 
            last_name="Plata", 
            name="Carlitos", 
            password="hashed_password")

        self.user_repository.get_user_by_email.return_value = existing_user
        with self.assertRaises(ConflictWithExistingResourceException):
            self.auth_service.signup(candidate)

        self.user_repository.get_user_by_email.assert_called_once_with(candidate.email)
        self.password_encryptor.get_password_hash.assert_not_called()
        self.user_repository.save_user.assert_not_called()
   

if __name__ == "__main__":
    unittest.main()
