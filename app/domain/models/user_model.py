from uuid import UUID


class UserModel:
    def __init__(
        self, 
        id: UUID | None, 
        name: str, 
        last_name: str, 
        email: str, 
        password: str, 
        profile_image: str | None = None
    ) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.profile_image = profile_image
