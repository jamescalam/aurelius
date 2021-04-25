from fastapi import FastAPI
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
from haystack.retriever.sparse import ElasticsearchRetriever
from haystack.reader.farm import FARMReader
from haystack.pipeline import ExtractiveQAPipeline

# initialize doc store, retriever and reader components
DOC_STORE = ElasticsearchDocumentStore(
    host='localhost', username='', password='', index='aurelius'
)
RETRIEVER = ElasticsearchRetriever(DOC_STORE)
READER = FARMReader(model_name_or_path='deepset/bert-base-cased-squad2',
                    context_window_size=1500,
                    use_gpu=True)
# initialize pipeline
PIPELINE = ExtractiveQAPipeline(reader=READER, retriever=RETRIEVER)
# initialize API
APP = FastAPI()

@APP.get('/query')
async def get_query(q: str, retriever_limit: int = 10, reader_limit: int = 3):
    """Makes query to doc store via Haystack pipeline.

    :param q: Query string representing the question being asked.
    :type q: str
    """
    # get answers
    return PIPELINE.run(query=q,
                        top_k_retriever=retriever_limit,
                        top_k_reader=reader_limit)