from uuid import UUID

class Cv:
    id: UUID
    name: str
    filelink: str
    category: str
    doc_id: UUID
    created_at: str

    def __init__(self, id, name, filelink, category, doc_id, created_at):
        self.id = id
        self.name = name
        self.filelink = filelink
        self.category = category
        self.doc_id = doc_id
        self.created_at = created_at.ctime()
    