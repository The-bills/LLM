from uuid import UUID
class Position:
    id: UUID
    name: str 
    description: str

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
