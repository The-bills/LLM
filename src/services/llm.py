from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage
from llama_index import VectorStoreIndex
from llama_index.node_parser import SimpleNodeParser

def process_cv(cv):
    #load index
    index = load_index()
    # load new file
    # load parse to nodes and add to index
    # save index
    index.storage_context.persist()

def query(index, query):
    query_engine = index.as_query_engine()
    return query_engine.query(query).response

def load_index():
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    return load_index_from_storage(storage_context)

def load_directory(folder_name):
    documents = SimpleDirectoryReader(folder_name).load_data()
    parser = SimpleNodeParser.from_defaults()
    nodes = parser.get_nodes_from_documents(documents)
    index = VectorStoreIndex(nodes)
    index.storage_context.persist()
    return index