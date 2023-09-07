import jsonpickle
from cv import Cv
import services.llm as llm

from flask import Blueprint

api = Blueprint('cv_api', __name__)

@api.route("/")
def all_cvs():
    return jsonpickle.encode(Cv.get_all())

@api.route("/<id>")
def get_cv(id):
    return jsonpickle.encode(Cv.iget_one(id))

@api.route("/", methods=['POST'])
def upload_cv():
    cv = jsonpickle.encode(Cv.insert())
    llm.process_cv(cv)
    return cv

@api.route("/<id>", methods=['DELETE'])
def delete_cv(id):
    return jsonpickle.encode(Cv.delete(id))

@api.route("/<id>/process", methods=['POST'])
def process_cv(id):
    cv = Cv.get_one(id)
    llm.process_cv(cv)
    return jsonpickle.encode({"success": True})
