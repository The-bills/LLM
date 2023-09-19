import jsonpickle
from repo import Repo
import services.rate as rate
from services.ChromaStore import ChromaStore
from llama_index.vector_stores.types import ExactMatchFilter

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
    position = Repo().Position.get_one(id)
    ChromaStore(collection_name='cvtest')
    res = ChromaStore.query(query=f"Find best candidate for this job and tell why. Job {position.name}: {position.description}", filters=[])
    return jsonpickle.encode(res.response)
