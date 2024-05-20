from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.application.services.auth_service import AuthService
from app.domain.exceptions.conflict_with_existing_resource_exception import (
    ConflictWithExistingResourceException,
)
from app.domain.exceptions.invalid_credentials_exception import (
    InvalidCredentialsException,
)
from app.infrastructure.dto.bearer_token_dto import BearerTokenDTO
from app.infrastructure.dto.candidate_dto import CandidateDTO
from app.infrastructure.dto.authenticated_user_dto import AuthenticatedUserDTO
from app.infrastructure.mappers.candidate_mappers import (
    map_candidate_dto_to_candidate_model,
)
from app.infrastructure.mappers.user_mappers import map_user_model_to_user_logged_dto
from app.infrastructure.repositories.relational_db_user_repository_impl import (
    RelationalDBUserRepositoryImpl,
)
from app.infrastructure.security.bcrypt_password_encryptor_impl import (
    BcryptPasswordEncryptorImpl,
)
from app.infrastructure.security.json_web_token_tools import JsonWebTokenTools


auth_router = APIRouter()
auth_service = AuthService(
    password_encryptor=BcryptPasswordEncryptorImpl(),
    user_repository=RelationalDBUserRepositoryImpl(),
)


@auth_router.post("/login", status_code=status.HTTP_200_OK)
def login_user(
    user_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> BearerTokenDTO:
    try:
        user = auth_service.login(email=user_data.username, password=user_data.password)

        return BearerTokenDTO(
            access_token=JsonWebTokenTools.create_access_token(user.email),
            user_email=user.email,
            user_id=str(user.id),
            user_last_name=user.last_name,
            user_name=user.name,
            user_profile_image=user.profile_image or "",
        )
    except InvalidCredentialsException:
        raise HTTPException(
            headers={"WWW-Authenticate": "Bearer"},
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup_user(candidate: CandidateDTO) -> BearerTokenDTO:
    try:
        user = auth_service.signup(map_candidate_dto_to_candidate_model(candidate))

        return BearerTokenDTO(
            access_token=JsonWebTokenTools.create_access_token(user.email),
            user_email=user.email,
            user_id=str(user.id),
            user_last_name=user.last_name,
            user_name=user.name,
            user_profile_image=user.profile_image or "",
        )
    except ConflictWithExistingResourceException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email address is already in use",
        )
