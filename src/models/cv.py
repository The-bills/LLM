from services.LlamaIndex import ChromaStore

class Cv:
    id: str
    name: str
    filelink: str
    inserted_at: str
    metadata: dict

    @staticmethod
    def from_chroma_format(raw, index = 0):
        cv = Cv()
        cv.metadata = raw['metadatas'][index]
        cv.id = cv.metadata['doc_id']
        del cv.metadata['_node_content']
        cv.name = cv.metadata['name']
        cv.filelink = cv.metadata['filelink']
        cv.inserted_at = cv.metadata['inserted_at']
        return cv

    @staticmethod
    def many_from_chroma_format(raw):
        cvs = []
        for index in range(len(raw['ids'])):
            cvs.append(Cv.from_chroma_format(raw, index))
        return cvs
    
    @staticmethod
    def get(id):
        raw = ChromaStore().collection.get(
            where={"doc_id": id},
            include=['metadatas']
        )
        return Cv.from_chroma_format(raw)
    
    @staticmethod
    def get_all():
        raw = ChromaStore().collection.get(
            where={"type": "cv"},
            include=['metadatas']
        )
        return Cv.many_from_chroma_format(raw)
        