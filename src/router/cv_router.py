import jsonpickle
import json
from repo import Repo
from flask import Blueprint, request
from utils.files import is_pdf
import resolvers.cv_resolver as cv_resolver
from services.ChromaStore import ChromaStore
from services.LlamaIndex import LlamaIndex

api = Blueprint('cv_api', __name__)

@api.route("/")
def get_all():
    res = ChromaStore().collection.get(
        where={"type": "cv"},
        include=['documents', 'metadatas']
        )
    return jsonpickle.encode(res, unpicklable=False)

@api.route("/<id>")
def get_one(id):
    res = ChromaStore().collection.get(
        where={"doc_id": id},
        include=['metadatas']
    )
    res_json = json.dumps(res, indent=2)
    return res_json


@api.route("/", methods=['POST'])
def insert():
    file = request.files['cv']
    if not is_pdf(file.filename):
        return jsonpickle.encode({"error": "Invalid file type"})

    res = cv_resolver.insert_cv(file)
    print(LlamaIndex().count_tokens_all())
    return jsonpickle.encode(res.__dict__, unpicklable=False)


@api.route("/<id>", methods=['DELETE'])
def delete(id):
    LlamaIndex().delete(id)
    return jsonpickle.encode({"status": "ok"}, unpicklable=False)
