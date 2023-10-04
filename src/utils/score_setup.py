from llama_index.prompts import PromptTemplate
from llama_index.prompts.default_prompts import DEFAULT_TEXT_QA_PROMPT_TMPL, DEFAULT_REFINE_PROMPT_TMPL
from llama_index.output_parsers import LangchainOutputParser
from langchain.output_parsers import StructuredOutputParser
from llama_index.vector_stores.types import ExactMatchFilter
from services.LlamaIndex import LlamaIndex
from langchain.output_parsers import CommaSeparatedListOutputParser

def query_setup(response_schemas: list, doc):
    filters = [ExactMatchFilter(key="doc_id", value=doc.doc_id)]
    lc_output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    res = setup_scoring("Answer schemas with maximally two words", filters, lc_output_parser)
    return res

def setup_scoring(query, filters, lc_output_parser=CommaSeparatedListOutputParser()):
    output_parser = LangchainOutputParser(lc_output_parser)
    fmt_qa_tmpl = output_parser.format(DEFAULT_TEXT_QA_PROMPT_TMPL)
    fmt_refine_tmpl = output_parser.format(DEFAULT_REFINE_PROMPT_TMPL)
    qa_prompt = PromptTemplate(fmt_qa_tmpl, output_parser=output_parser)
    refine_prompt = PromptTemplate(fmt_refine_tmpl, output_parser=output_parser)
    res = LlamaIndex().query(query, filters=filters, text_qa_template=qa_prompt, refine_prompt_template=refine_prompt).response
    return output_parser.parse(res)