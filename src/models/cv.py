from uuid import UUID

class Cv:
    id: UUID
    name: str
    filelink: str
    category: str
    doc_id: UUID

    def __init__(self, id, name, filelink, category, doc_id):
        self.id = id
        self.name = name
        self.filelink = filelink
        self.category = category
        self.doc_id = doc_id
    