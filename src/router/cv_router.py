import jsonpickle
from repo import Repo
import services.llm as llm

from flask import Blueprint, request

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
    category = request.form['category']
    file.save(file.filename)
    cv = Repo.Cv.insert("Unknown", category)
    # llm.process_cv(cv)
    return jsonpickle.encode(cv)

@api.route("/<id>", methods=['DELETE'])
def delete_cv(id):
    return jsonpickle.encode(Repo.Cv.delete(id))

@api.route("/<id>/process", methods=['POST'])
def process_cv(id):
    cv = Repo.Cv.get_one(id)
    llm.process_cv(cv)
    return jsonpickle.encode({"success": True})
