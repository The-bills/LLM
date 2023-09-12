from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings import LangchainEmbedding
from llama_index.vector_stores.types import MetadataFilters
import chromadb
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


class ChromaStore:
    _instance = None

    def __new__(cls, collection_name:str,path="FOLDER_PATH_CHROMA_DB"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
            #Połączenie
            cls._instance.chroma_client = chromadb.PersistentClient(path=path)
            cls._instance.chroma_collection = cls._instance.chroma_client.get_or_create_collection(collection_name)
            cls._instance.vector_store = ChromaVectorStore(chroma_collection=cls._instance.chroma_collection)
            cls._instance.storage_context = StorageContext.from_defaults(vector_store=cls._instance.vector_store)

            #Embedding
            cls._instance.embed_model = LangchainEmbedding(
                HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2"),
            )

            cls._instance.service_contest = ServiceContext.from_defaults(embed_model=cls._instance.embed_model)
            cls._instance.index = VectorStoreIndex.from_vector_store(vector_store=cls._instance.vector_store,
                                                                     service_context=cls._instance.service_contest)
    
        return cls._instance

    # @staticmethod
    def insert_doc(path: str, metadata_name: list): #Czy to lista ma być?
        documents = SimpleDirectoryReader('FOLDER_PATH').load_data()
        for (document, metadata_name) in zip(documents, metadata_name):
            document.metadata = {"name": metadata_name}    
            ChromaStore._instance.index.insert(document)
        return ChromaStore._instance.index

    def delete_doc(ids_name: str):
        doc_to_delete = ChromaStore._instance.chroma_collection.get(limit=1)
        ChromaStore._instance.chroma_collection.delete(
            ids=[doc_to_delete[ids_name][0]]
        )
        
    @staticmethod
    def _query_engine(filters): 
        engine_filters = MetadataFilters(filters=filters)
        query_engine = ChromaStore._instance.index.as_query_engine(filters=engine_filters)
        return query_engine

    @staticmethod
    def query(query: str, filters):
        response = ChromaStore._query_engine(filters=filters).query(query=query)
        return response
    