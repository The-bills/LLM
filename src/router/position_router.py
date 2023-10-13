import jsonpickle
from services.ChromaStore import ChromaStore
from flask import Blueprint, request
from resolvers import position_resolver
from services.LlamaIndex import LlamaIndex
from utils.score_setup import setup_scoring
from utils.tiktoken import count_tokens
from utils.extract_from_dic import extract_name_from_dict
from llama_index.vector_stores.types import ExactMatchFilter

api = Blueprint('position_api', __name__)

@api.route("/")
def get_positions():
    res = ChromaStore().collection.get(where={"type": "position"}, include=['documents', 'metadatas'])
    return jsonpickle.encode(res, unpicklable=False)


@api.route("/<id>")
def get_position(id):
    res = ChromaStore().collection.get(where={"doc_id": id}, include=['documents', 'metadatas'])
    return jsonpickle.encode(res, unpicklable=False)


@api.route("/<id>", methods=['DELETE'])
def delete_position(id):
    LlamaIndex().delete(id)
    return jsonpickle.encode({"status": "ok"}, unpicklable=False)


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
    res_name = extract_name_from_dict(res)
    return res_name
    # return jsonpickle.encode(res, unpicklable=False)
    
@api.route("/<positionId>/match2", methods=['GET'])
def match_position_to_cv2(positionId):
    raw_position = ChromaStore().collection.get(where={"doc_id": positionId}, include=['documents'])
    position = raw_position['documents'][0]
    query_string = f"""
    Który kandydat jest najlepszy na podane stanowisko?
    Wymień imiona i nazwiska osób, które nalezy brać pod uwagę oraz wyniki jakie uzyskali  w formacie imie-wynik
    Pozycja:
    ```
    {position}
    ```
    """
    filters = [ExactMatchFilter(key="type", value="cv")]
    res = setup_scoring(query_string, filters)
    return jsonpickle.encode(res, unpicklable=False)

