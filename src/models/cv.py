class Cv:
    id: str
    name: str
    filelink: str
    category: str

    def __init__(self, id, name, filelink, category):
        self.id = id
        self.name = name
        self.filelink = filelink
        self.category = category
    