from uuid import UUID


class MarkerModel:
    def __init__(
        self,
        id: UUID | None,
        incident_id: UUID | None,
        latitude: float,
        longitude: float,
        direction: str,
    ):
        self.id = id
        self.incident_id = incident_id
        self.latitude = latitude
        self.longitude = longitude
        self.direction = direction
