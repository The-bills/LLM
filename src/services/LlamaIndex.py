from llama_index import VectorStoreIndex, ServiceContext
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings import LangchainEmbedding
from llama_index.vector_stores.types import MetadataFilters
from llama_index.schema import Document
from services.ChromaStore import ChromaStore

class LlamaIndex:
    _instance = None
    chroma: ChromaStore
    index: VectorStoreIndex

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            
            # Chroma
            cls.chroma = ChromaStore()
            cls.vector_store = ChromaVectorStore(chroma_collection=cls.chroma.collection)
            cls.storage_context = StorageContext.from_defaults(vector_store=cls.vector_store)

            # Embedding
            cls.embed_model = LangchainEmbedding(
                HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2"),
            )

            cls.service_context = ServiceContext.from_defaults(embed_model=cls.embed_model)
            cls.index = VectorStoreIndex.from_vector_store(vector_store=cls.vector_store,
                                                                     service_context=cls.service_context)
    
        return cls._instance

    def insert(self, document: Document):
        self.index.insert(document)
    
    def update(self, document: Document):
        self.index.update_ref_doc(document)
    
    def delete(self, doc_id: str):
        self.index.delete_ref_doc(doc_id)
    
    def query(self, query: str, filters, text_qa_template=None, refine_prompt_template=None):
        response = self._query_engine(
            filters=filters, text_qa_template=text_qa_template,refine_prompt_template=refine_prompt_template
            ).query(query)
        return response

    def _query_engine(self, filters, text_qa_template=None, refine_prompt_template=None): 
        engine_filters = MetadataFilters(filters=filters)
        query_engine = self.index.as_query_engine(
            filters=engine_filters, text_qa_template=text_qa_template,refine_prompt_template=refine_prompt_template
            )
        return query_engine

    