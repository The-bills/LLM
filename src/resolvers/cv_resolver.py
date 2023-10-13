from services.file_storage import FileStorage
from llama_index.schema import Document
from llama_index import SimpleDirectoryReader 
from services.process_cv import process_cv
from werkzeug.datastructures import FileStorage as File
from services.LlamaIndex import LlamaIndex
from datetime import datetime
from models.cv import Cv

def insert_cv(file: File) -> Document:
    filelink = FileStorage.save(file)
    document = SimpleDirectoryReader(input_files=[filelink]).load_data()[0]
    document.metadata = {"type": "cv", "filelink": filelink, "inserted_at": datetime.now().isoformat()}
    LlamaIndex().insert(document)
    process_cv(document)
    return Cv.get(document.doc_id)
