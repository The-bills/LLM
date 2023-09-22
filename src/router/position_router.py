import jsonpickle
from repo import Repo
# import services.rate as rate
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
    # position = Repo().Position.get_one(id)
    position_id = 'fad82f72-f74e-49a7-8bde-03a71cf905f0'
    # collection.query where type="cv" and embedings = emedings(position_id)
    ChromaStore(collection_name="cv_test")
    # embeddings = ChromaStore._get_embeddings(position_id)
    # res = ChromaStore.query_collection(embeddings["embeddings"])
    # print(res)
    # res = ChromaStore.query(query=f"Find best candidate for this job and tell why. Job {position.name}: {position.description}", filters=[])
    # return jsonpickle.encode(res.response)
    return jsonpickle.encode(ChromaStore._instance.chroma_collection.get(ids=['19772704-cd9d-4721-a76b-0fcdeb041409']))
    # return "ok"


#fad82f72-f74e-49a7-8bde-03a71cf905f0