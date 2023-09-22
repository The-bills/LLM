import jsonpickle
from repo import Repo
from flask import Blueprint, request
from services.file_storage import FileStorage
from utils.files import is_pdf
from services.ChromaStore import ChromaStore
from llama_index.vector_stores.types import ExactMatchFilter

api = Blueprint('cv_api', __name__)

@api.route("/")
def all_cvs():
    return jsonpickle.encode(Repo.Cv.get_all())

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
    name = ChromaStore.query("What is a name of this person? Returny ONLY full name", filters=[ExactMatchFilter(key="doc_id", value=doc.doc_id)]).response
    print(name)
    cv = Repo.Cv.insert(name, filelink, request.form['category'], doc.doc_id)
    return jsonpickle.encode(cv)

@api.route("/<id>", methods=['DELETE'])
def delete_cv(id):
    return jsonpickle.encode(Repo.Cv.delete(id))
