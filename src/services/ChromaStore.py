from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings import LangchainEmbedding
from llama_index.vector_stores.types import MetadataFilters
from chromadb import PersistentClient
from llama_index.schema import Document

class ChromaStore:
    _instance = None

    def __new__(cls, collection_name:str = 'default',path="FOLDER_PATH_CHROMA_DB"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls.client = PersistentClient(path=path)
            cls.collection = cls.client.get_or_create_collection(collection_name)
        return cls._instance

    def query_collection(self, embeddings):
        return self.collection.query(
            query_embeddings=embeddings,
            n_results=1,
            include=["metadatas", "distances"],
            where={"type": "cv"}
        )
    
    # def match()
