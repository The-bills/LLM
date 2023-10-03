import jsonpickle
from repo import Repo
# import services.rate as rate
from services.ChromaStore import ChromaStore
from llama_index.vector_stores.types import ExactMatchFilter

from flask import Blueprint, request
from resolvers import position_resolver

api = Blueprint('position_api', __name__)

@api.route("/")
def get_positions():
    res = ChromaStore().collection.get(where={"type": "position"}, include=['documents', 'metadatas'])
    return jsonpickle.encode(res, unpicklable=False)

@api.route("/<id>")
def get_position(id):
    res = ChromaStore().collection.get(where={"doc_id": id}, include=['documents', 'metadatas'])
    return jsonpickle.encode(res, unpicklable=False)


# @api.route("/<id>/scores")
# def score_position(id):
#     # position = Repo().Position.get_one(id)
#     position_id = 'fad82f72-f74e-49a7-8bde-03a71cf905f0'
#     # collection.query where type="cv" and embedings = emedings(position_id)
#     ChromaStore(collection_name="cv_test")
#     doc = ChromaStore.insert_doc('uploads/position1.txt')
#     # embeddings = ChromaStore._get_embeddings(position_id)
#     print(doc)
#     return jsonpickle.encode(doc)
#     # res = ChromaStore.query_collection(embeddings["embeddings"])
#     # print(res)
#     # res = ChromaStore.query(query=f"Find best candidate for this job and tell why. Job {position.name}: {position.description}", filters=[])
#     # return jsonpickle.encode(res.response)
#     return jsonpickle.encode(ChromaStore._instance.chroma_collection.get(ids=['19772704-cd9d-4721-a76b-0fcdeb041409']))
#     # return "ok"


#fad82f72-f74e-49a7-8bde-03a71cf905f0
@api.route("/", methods=['POST'])
def add_position():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return 'Invalid Content-Type'
    
    name = request.json["name"]
    description = request.json['description']

    if not name or not description:
        return 'Invalid body format'

    res = position_resolver.add_position(name, description)
    return jsonpickle.encode(res.__dict__, unpicklable=False)

@api.route("/<positionId>/match", methods=['GET'])
def match_position_to_cv(positionId):
    embedings = ChromaStore().collection.get(where={'doc_id': positionId}, include=['embeddings'])['embeddings'][0]
    res = ChromaStore().query_collection(embedings)
    print(res)
    return 'ok'
    

