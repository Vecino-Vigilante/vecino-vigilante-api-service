from pydantic import BaseModel


class BearerTokenDTO(BaseModel):
    access_token: str
    token_type: str = "bearer"
