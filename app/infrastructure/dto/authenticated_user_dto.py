from uuid import UUID
from pydantic import BaseModel, EmailStr


class AuthenticatedUserDTO(BaseModel):
    id: UUID
    name: str
    last_name: str
    email: EmailStr
