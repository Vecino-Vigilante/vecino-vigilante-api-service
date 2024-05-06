from os import getenv
from pydantic import BaseModel


class MicroserviceInfoDTO(BaseModel):
    microservice_name: str
    microservice_summary: str
    microservice_version: str
    microservice_developer: str
    microservice_developer_email: str

    def __init__(self) -> None:
        super().__init__(
            microservice_name=getenv("MICROSERVICE_NAME"),
            microservice_summary=getenv("MICROSERVICE_SUMMARY"),
            microservice_version=getenv("MICROSERVICE_VERSION"),
            microservice_developer=getenv("MICROSERVICE_DEVELOPER"),
            microservice_developer_email=getenv("MICROSERVICE_DEVELOPER_EMAIL"),
        )
