from fastapi import FastAPI
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever

DOC_STORE = ElasticsearchDocumentStore(
    host='localhost', username='', password='', index='aurelius'
)
RETRIEVER = ElasticsearchRetriever(DOC_STORE)
APP = FastAPI()

@APP.get('/query')
async def get_query():
    """Makes query to doc store via retriever.

    TODO: include query as parameter
    TODO: update to implement full pipeline including reader
    """
    return RETRIEVER.retrieve('Physics is a very abstract subject')