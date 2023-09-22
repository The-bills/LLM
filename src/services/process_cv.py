from llama_index.prompts import PromptTemplate
from services.ChromaStore import ChromaStore
from llama_index.prompts.default_prompts import DEFAULT_TEXT_QA_PROMPT_TMPL, DEFAULT_REFINE_PROMPT_TMPL
from llama_index.output_parsers import LangchainOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from llama_index.vector_stores.types import ExactMatchFilter

def process_cv(doc):
    metadata = assign_metadata(doc)
    score = assign_score(doc)
    doc.metadata = {"type": "cv"} | metadata | score
    ChromaStore._instance.chroma_collection.update(
        ids=[doc.doc_id],
        metadatas=[{"type": "cv"}]
    )

def assign_metadata(doc):
    response_schemas = [
        ResponseSchema(name="name", description="Describes the author's name."),
        ResponseSchema(name="education", description="Describes the author's educational experience/background level.")
    ]
    lc_output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    output_parser = LangchainOutputParser(lc_output_parser)
    fmt_qa_tmpl = output_parser.format(DEFAULT_TEXT_QA_PROMPT_TMPL)
    fmt_refine_tmpl = output_parser.format(DEFAULT_REFINE_PROMPT_TMPL)
    qa_prompt = PromptTemplate(fmt_qa_tmpl, output_parser=output_parser)
    refine_prompt = PromptTemplate(fmt_refine_tmpl, output_parser=output_parser)
    metadata = ChromaStore.query("Answer schemas with maximally two words", filters=[ExactMatchFilter(key="doc_id", value=doc.doc_id)], text_qa_template=qa_prompt, refine_prompt_template=refine_prompt).response
    return output_parser.parse(metadata)

def assign_score(doc):
    response_schemas = [
        ResponseSchema(name="experience_score", description="Rates canditate experience from Cv on scale 1-10"),
        ResponseSchema(name="education_score", description="Rates canditate educational performance from Cv on scale 1-10"),
        # ResponseSchema(name="Education", description="Rates canditate educational performance from Cv on scale 1-10"),
        # ResponseSchema(name="Education", description="Rates canditate educational performance from Cv on scale 1-10")
    ]
    lc_output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    output_parser = LangchainOutputParser(lc_output_parser)
    fmt_qa_tmpl = output_parser.format(DEFAULT_TEXT_QA_PROMPT_TMPL)
    fmt_refine_tmpl = output_parser.format(DEFAULT_REFINE_PROMPT_TMPL)
    qa_prompt = PromptTemplate(fmt_qa_tmpl, output_parser=output_parser)
    refine_prompt = PromptTemplate(fmt_refine_tmpl, output_parser=output_parser)
    metadata = ChromaStore.query("Answer schemas with maximally two words", filters=[ExactMatchFilter(key="doc_id", value=doc.doc_id)], text_qa_template=qa_prompt, refine_prompt_template=refine_prompt).response
    return output_parser.parse(metadata)
    