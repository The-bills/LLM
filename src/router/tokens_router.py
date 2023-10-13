import jsonpickle
import json
from repo import Repo
from flask import Blueprint, request
from utils.files import is_pdf
import resolvers.cv_resolver as cv_resolver
from services.ChromaStore import ChromaStore
from services.LlamaIndex import LlamaIndex

api = Blueprint('tokens_api', __name__)


@api.route("/tokens", methods=['GET'])
def count_tokens():
    tokens = LlamaIndex().count_tokens_all() 
    return jsonpickle.encode(tokens, unpicklable=False)

@api.route("/tokens", methods=["POST"])
def reset_tokens():
    tokens = LlamaIndex().reset_tokens()
    return jsonpickle.encode(tokens, unpicklable=False)
