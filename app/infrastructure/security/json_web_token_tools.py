from os import getenv
from jose import jwt
from datetime import datetime, timedelta, timezone


class JsonWebTokenTools:
    __ALGORITHM = getenv("JWT_ALGORITHM", "")
    __SECRET_KEY = getenv("JWT_SECRET_KEY", "")

    @staticmethod
    def create_access_token(username: str):
        expires_on = datetime.now(timezone.utc) + timedelta(minutes=180)
        payload = {"sub": username, "exp": expires_on}

        return jwt.encode(
            payload,
            JsonWebTokenTools.__SECRET_KEY,
            algorithm=JsonWebTokenTools.__ALGORITHM,
        )

    @staticmethod
    def validate_access_token(token: str):
        payload = jwt.decode(
            token,
            JsonWebTokenTools.__SECRET_KEY,
            algorithms=[JsonWebTokenTools.__ALGORITHM],
        )

        return payload
