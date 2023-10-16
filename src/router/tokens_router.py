import jsonpickle
import json
from repo import Repo
from flask import Blueprint, request
from utils.files import is_pdf
import resolvers.cv_resolver as cv_resolver
from services.ChromaStore import ChromaStore
from services.LlamaIndex import LlamaIndex

api = Blueprint('tokens_api', __name__)


@api.route("/embedding", methods=['GET'])
def count_tokens():
    tokens = LlamaIndex().count_tokens_all() 
    return jsonpickle.encode(tokens, unpicklable=False)

@api.route("/llm", methods=['GET'])
def count_tokens_llm():
    tokens = LlamaIndex().count_tokens_all_prompt() 
    return jsonpickle.encode(tokens, unpicklable=False)

@api.route("/", methods=["DELETE"])
def reset_tokens():
    LlamaIndex().reset_tokens()
    return jsonpickle.encode({"status": "ok"}, unpicklable=False)
