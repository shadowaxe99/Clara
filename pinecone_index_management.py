```python
import pinecone

PINECONE_API_KEY = "your_pinecone_api_key"
PINECONE_ENVIRONMENT = "your_pinecone_environment"
YOUR_TABLE_NAME = "your_table_name"

def manage_pinecone_index():
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
    table_name = YOUR_TABLE_NAME
    dimension = 1536
    metric = "cosine"
    pod_type = "p1"
    if table_name not in pinecone.list_indexes():
        pinecone.create_index(table_name, dimension=dimension, metric=metric, pod_type=pod_type)
    index = pinecone.Index(table_name)
    return index

if __name__ == "__main__":
    manage_pinecone_index()
```