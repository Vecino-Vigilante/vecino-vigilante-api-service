from uuid import UUID

class ComplaintTypeModel:
    def __init__(self, id: UUID, name: str):
        self.id = id
        self.name = name