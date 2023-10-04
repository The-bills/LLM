from llama_index.prompts import PromptTemplate
from llama_index.prompts.default_prompts import DEFAULT_TEXT_QA_PROMPT_TMPL, DEFAULT_REFINE_PROMPT_TMPL
from llama_index.output_parsers import LangchainOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from llama_index.vector_stores.types import ExactMatchFilter
from services.LlamaIndex import LlamaIndex
from llama_index.schema import Document
from utils.score_setup import query_setup

def process_position(doc: Document):
    score = assign_score(doc)
    doc.metadata = doc.metadata | score
    LlamaIndex().update(doc)


def assign_score(doc):
    response_schemas = [
        ResponseSchema(name="experience_score", description="Rates experience required on this postion on scale 1-10"),
    ]
    res = query_setup(response_schemas=response_schemas, doc=doc)
    return res
    