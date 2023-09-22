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

            # cls._instance.chroma_collection.query()

            #Embedding
            cls._instance.embed_model = LangchainEmbedding(
                HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2"),
            )

            cls._instance.service_contest = ServiceContext.from_defaults(embed_model=cls._instance.embed_model)
            cls._instance.index = VectorStoreIndex.from_vector_store(vector_store=cls._instance.vector_store,
                                                                     service_context=cls._instance.service_contest)
    
        return cls._instance

    # @staticmethod
    def insert_doc(path: str, metadata = {}):
        document = SimpleDirectoryReader(input_files=[path]).load_data()[0]
        document.metadata = metadata | {"type": "cv"}
        ChromaStore._instance.index.insert(document)
        return document

    def delete_doc(ids_name: str):
        doc_to_delete = ChromaStore._instance.chroma_collection.get(limit=1)
        ChromaStore._instance.chroma_collection.delete(
            ids=[doc_to_delete[ids_name][0]]
        )

    @staticmethod
    def _query_engine(filters, text_qa_template=None, refine_prompt_template=None): 
        engine_filters = MetadataFilters(filters=filters)
        query_engine = ChromaStore._instance.index.as_query_engine(
            filters=engine_filters, text_qa_template=text_qa_template,refine_prompt_template=refine_prompt_template
            )
        return query_engine

    @staticmethod
    def query(query: str, filters, text_qa_template=None, refine_prompt_template=None):
        response = ChromaStore._query_engine(
            filters=filters, text_qa_template=text_qa_template,refine_prompt_template=refine_prompt_template
            ).query(query)
        return response
    
    def _get_embeddings(id):
       return ChromaStore._instance.chroma_collection.get(
           ids=[id],
           include=["embeddings"]

       )

    def query_collection(embeddings):
        return ChromaStore._instance.chroma_collection.query(
            query_embeddings=embeddings,
            n_results=1,
            include=["embeddings", "documents", "metadatas", "distances"],
            where={"type": "cv"}
        )
