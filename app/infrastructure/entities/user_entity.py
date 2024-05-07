from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_name: str
    email: str = Field(unique=True)
    password: str
    profile_image: str | None = Field(default=None)
