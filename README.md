# Aurelius

Fun Q&A project building Stoic AI

## Notes

### Running API

Navigate to `/qa_service` and type:

```
uvicorn api:APP --reload
```

### ImportError on Windows
To fix `ImportError` on Windows due to lack of FAISS (`_swigfaiss`), edit the `__init__.py` file found in:

```
~/AppData/Local/Programs/Python/Python39/Lib/site-packages/haystack/document_store
```

and comment out the FAISS import, which will leave the file looking like:

```
from haystack.document_store.elasticsearch import ElasticsearchDocumentStore
#from haystack.document_store.faiss import FAISSDocumentStore
from haystack.document_store.memory import InMemoryDocumentStore
from haystack.document_store.milvus import MilvusDocumentStore
from haystack.document_store.sql import SQLDocumentStore
```