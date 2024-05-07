from jose import JWTError
from typing import Annotated
from fastapi import Depends, HTTPException, status

from app.infrastructure.dto.authenticated_user_dto import AuthenticatedUserDTO
from app.infrastructure.repositories.relational_database_user_repository_impl import (
    RelationalDatabaseUserRepositoryImpl,
)
from app.infrastructure.security.security_scheme import SECURITY_SCHEME
from app.infrastructure.security.json_web_token_tools import JsonWebTokenTools


async def protect_route_middlware(token: Annotated[str, Depends(SECURITY_SCHEME)]):
    credentials_exception = HTTPException(
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
        status_code=status.HTTP_401_UNAUTHORIZED,
    )

    try:
        token_payload = JsonWebTokenTools.validate_access_token(token)

        user_email = token_payload.get("sub")

        if user_email is None:
            raise credentials_exception

        user_repository = RelationalDatabaseUserRepositoryImpl()
        user = user_repository.get_user_by_email(user_email)

        if user is None or not user.id:
            raise credentials_exception

        return AuthenticatedUserDTO(
            email=user.email, id=user.id, last_name=user.last_name, name=user.name
        )
    except JWTError:
        raise credentials_exception
