class Cv:
    id: str
    name: str
    content: str
    filelink: str

    def __init__(self, id, name, filelink, content):
        self.id = id
        self.name = name
        self.filelink = filelink
        self.content = content
    