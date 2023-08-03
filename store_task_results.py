```python
import pinecone
from get_ada_embedding import get_ada_embedding

def store_task_results(task, result, index):
    enriched_result = {'data': result}
    result_id = f"result_{task['task_id']}"
    vector = enriched_result['data']
    index.upsert([(result_id, get_ada_embedding(vector), {"task": task['task_name'], "result": result})])
```