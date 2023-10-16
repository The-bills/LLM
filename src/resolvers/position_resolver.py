from llama_index.schema import Document
from services.process_position import process_position
from services.LlamaIndex import LlamaIndex
from datetime import datetime

def add_position(name, description) -> Document:
    document = Document()
    document.set_content(f"{name} \n {description}")
    document.metadata = {"type": "position", "name": name, "inserted_at": datetime.now().isoformat()}
    LlamaIndex().insert(document)
    process_position(document)
    return document
