from pydantic import BaseModel, EmailStr


class AuthenticatedUserDTO(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr
