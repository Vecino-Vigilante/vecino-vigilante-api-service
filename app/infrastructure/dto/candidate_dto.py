from pydantic import BaseModel, EmailStr, SecretStr


class CandidateDTO(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    password: SecretStr
