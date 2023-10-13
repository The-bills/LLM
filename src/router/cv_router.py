import jsonpickle
from flask import Blueprint, request
from utils.files import is_pdf
import resolvers.cv_resolver as cv_resolver
from services.LlamaIndex import LlamaIndex
from models.cv import Cv

api = Blueprint('cv_api', __name__)

@api.route("/")
def get_all():
    res = Cv.get_all()
    return jsonpickle.encode(res, unpicklable=False)

@api.route("/<id>")
def get_one(id):
    res = Cv.get(id)
    return jsonpickle.encode(res, unpicklable=False)


@api.route("/", methods=['POST'])
def insert():
    file = request.files['cv']
    if not is_pdf(file.filename):
        return jsonpickle.encode({"error": "Invalid file type"})

    res = cv_resolver.insert_cv(file)
    print(LlamaIndex().count_tokens_all())
    return jsonpickle.encode(res, unpicklable=False)


@api.route("/<id>", methods=['DELETE'])
def delete(id):
    LlamaIndex().delete(id)
    return jsonpickle.encode({"status": "ok"}, unpicklable=False)
