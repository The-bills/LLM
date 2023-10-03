from llama_index.schema import Document
from services.process_position import process_position
from services.LlamaIndex import LlamaIndex

def add_position(name, description) -> Document:
    document = Document()
    document.set_content(
        f"name: {name}, description: {description}"
        )
    document.metadata = {"type": "position"}
    LlamaIndex().insert(document)
    process_position(document)
    return document
