from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage
from llama_index import VectorStoreIndex
from llama_index.node_parser import SimpleNodeParser

def query(index, query):
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)

def load_index():
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    return load_index_from_storage(storage_context)

def load_to_storage(folder_name):
    documents = SimpleDirectoryReader(folder_name).load_data()
    parser = SimpleNodeParser.from_defaults()
    nodes = parser.get_nodes_from_documents(documents)
    index = VectorStoreIndex(nodes)
    index.storage_context.persist()


#index = load_index()
#query(index, "For each candidate determine if they are junior, mid or senior")

from cv import Cv
import jsonpickle
from flask import Flask

app = Flask(__name__)

@app.route("/cv")
def all_cvs():
    return jsonpickle.encode(Cv.get_all())

@app.route("/cv/<id>")
def get_cv(id):
    return jsonpickle.encode(Cv.get_one(id))

@app.route("/cv", methods=['POST'])
def upload_cv():
    return jsonpickle.encode(Cv.insert())

@app.route("/cv/<id>", methods=['DELETE'])
def delete_cv(id):
    return jsonpickle.encode(Cv.delete(id))

