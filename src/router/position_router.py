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
    position_id = 'c47ed888-6898-431c-a8d3-206771b379dd'
    ChromaStore(collection_name="cv_test")
    res = ChromaStore._instance.chroma_collection.get(where={"doc_id": position_id}, include=['metadatas'])
    # '843f2732-8e53-4191-bf6f-9fad15f4da92', '88fe6631-8eba-4929-88f1-707da96d4b8a
    # res = ChromaStore._instance.chroma_collection.get(ids = ['ebb964ac-91ca-495c-8312-56876ba4219b'])
    print(res)
    # return jsonpickle.encode(Repo.Position.get_one(id))
    return jsonpickle.encode(res)

@api.route("/<id>/scores")
def score_position(id):
    # position = Repo().Position.get_one(id)
    position_id = 'fad82f72-f74e-49a7-8bde-03a71cf905f0'
    # collection.query where type="cv" and embedings = emedings(position_id)
    ChromaStore(collection_name="cv_test")
    doc = ChromaStore.insert_doc('uploads/position1.txt')
    # embeddings = ChromaStore._get_embeddings(position_id)
    print(doc)
    return jsonpickle.encode(doc)
    # res = ChromaStore.query_collection(embeddings["embeddings"])
    # print(res)
    # res = ChromaStore.query(query=f"Find best candidate for this job and tell why. Job {position.name}: {position.description}", filters=[])
    # return jsonpickle.encode(res.response)
    return jsonpickle.encode(ChromaStore._instance.chroma_collection.get(ids=['19772704-cd9d-4721-a76b-0fcdeb041409']))
    # return "ok"


#fad82f72-f74e-49a7-8bde-03a71cf905f0