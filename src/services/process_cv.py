from langchain.output_parsers import ResponseSchema
from services.LlamaIndex import LlamaIndex
from utils.score_setup import query_setup

def process_cv(doc):
    metadata = assign_metadata(doc)
    score = assign_score(doc)
    doc.metadata = {"type": "cv"} | metadata | score
    LlamaIndex().update(doc)

def assign_metadata(doc):
    doc.excluded_embed_metadata_keys = ['name', 'education']
    response_schemas = [
        ResponseSchema(name="name", description="Describes the author's name."),
        ResponseSchema(name="education", description="Describes the author's educational experience/background level.")
    ]
    res = query_setup(response_schemas=response_schemas, doc=doc)
    return res

def assign_score(doc):
    response_schemas = [
        ResponseSchema(name="experience_score", description="Rates canditate experience from Cv on scale 1-10"),
        ResponseSchema(name="education_score", description="Rates canditate educational performance from Cv on scale 1-10"),
    ]
    res = query_setup(response_schemas=response_schemas, doc=doc)
    return res
