import jsonpickle
from llama_index.prompts import PromptTemplate
from repo import Repo
from flask import Blueprint, request
from services.file_storage import FileStorage
from utils.files import is_pdf
from services.ChromaStore import ChromaStore
from llama_index.vector_stores.types import ExactMatchFilter


from llama_index.output_parsers import LangchainOutputParser
from llama_index.prompts.default_prompts import DEFAULT_TEXT_QA_PROMPT_TMPL, DEFAULT_REFINE_PROMPT_TMPL
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from services.process_cv import process_cv

api = Blueprint('cv_api', __name__)

@api.route("/")
def all_cvs():
    # return jsonpickle.encode(Repo.Cv.get_all())
    ChromaStore(collection_name='cv_test')
    return jsonpickle.encode(ChromaStore._instance.chroma_collection.get())

@api.route("/<id>")
def get_cv(id):
    return jsonpickle.encode(Repo.Cv.get_one(id))

@api.route("/", methods=['POST'])
def upload_cv():
    file = request.files['cv']
    if not is_pdf(file.filename):
        return jsonpickle.encode({"error": "Invalid file type"})

    filelink = FileStorage.save(file)
    ChromaStore(collection_name='cv_test')
    doc = ChromaStore.insert_doc(filelink)
    process_cv(doc)
    # update doc
    print(doc)
    # cv = Repo.Cv.insert(name, filelink, request.form['category'], doc.doc_id)
    # return jsonpickle.encode(cv)
    return "ok"

@api.route("/<id>", methods=['DELETE'])
def delete_cv(id):
    return jsonpickle.encode(Repo.Cv.delete(id))
