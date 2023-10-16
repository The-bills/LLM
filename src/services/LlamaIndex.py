from llama_index import VectorStoreIndex, ServiceContext, set_global_service_context
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings import LangchainEmbedding
from llama_index.vector_stores.types import MetadataFilters
from llama_index.schema import Document
from services.ChromaStore import ChromaStore
import tiktoken
from llama_index.llms import Anthropic
from llama_index.callbacks import CallbackManager, TokenCountingHandler

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
            
            # Token handler
            cls.token_counter = TokenCountingHandler(
            tokenizer=tiktoken.encoding_for_model("gpt-3.5-turbo").encode
            )
            cls.callback_manager = CallbackManager([cls.token_counter])

            #ServiceContext/VectorStore
            cls.service_context = ServiceContext.from_defaults(
                embed_model=cls.embed_model,
                callback_manager=cls.callback_manager)
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

    def count_tokens_all(self):
        all_tokens = self.token_counter.total_embedding_token_count
        return all_tokens

    def count_tokens_all_prompt(self):
        prompt_tokens = self.token_counter.total_llm_token_count
        return prompt_tokens
    
    def reset_tokens(self):
        self.token_counter.reset_counts()

    @staticmethod
    def count_tokens_prompt(prompt, encoding_name="cl100k_base"):
            encoding = tiktoken.get_encoding(encoding_name)
            num_tokens = len(encoding.encode(prompt))
            return num_tokens
    