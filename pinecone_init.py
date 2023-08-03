```python
import pinecone

def initialize_pinecone(PINECONE_API_KEY, PINECONE_ENVIRONMENT, YOUR_TABLE_NAME):
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
    dimension = 1536
    metric = "cosine"
    pod_type = "p1"
    if YOUR_TABLE_NAME not in pinecone.list_indexes():
        pinecone.create_index(YOUR_TABLE_NAME, dimension=dimension, metric=metric, pod_type=pod_type)
    index = pinecone.Index(YOUR_TABLE_NAME)
    return index
```