import jsonpickle
from repo import Repo
import services.rate as rate

from flask import Blueprint

api = Blueprint('position_api', __name__)

@api.route("/")
def get_positions():
    return jsonpickle.encode(Repo.Position.get_all())

@api.route("/<id>")
def get_position(id):
    return jsonpickle.encode(Repo.Position.get_one(id))

@api.route("/<id>/scores")
def score_position(id):
    return jsonpickle.encode(rate.rate_position(id))
