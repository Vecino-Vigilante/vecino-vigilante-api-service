from fastapi import APIRouter

from ..dto.microservice_info_dto import MicroserviceInfoDTO

management_router = APIRouter()


@management_router.get("/info")
def get_microservice_information() -> MicroserviceInfoDTO:
    return MicroserviceInfoDTO()
