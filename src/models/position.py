from uuid import UUID
class Position:
    id: str
    name: str 
    description: str
    inserted_at: str

    @staticmethod
    def from_chroma_format(raw, index = 0):
        position = Position()
        position.metadata = raw['metadatas'][index]
        position.id = position.metadata['doc_id']
        del position.metadata['_node_content']
        position.name = position.metadata['name']
        position.inserted_at = position.metadata['inserted_at']
        position.description = raw['documents'][0]
        return position

    @staticmethod
    def many_from_chroma_format(raw):
        positions = []
        for index in range(len(raw['ids'])):
            positions.append(Position.from_chroma_format(raw, index))
        return positions
