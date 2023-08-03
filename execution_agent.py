```python
import openai
from context_agent import context_agent
from get_ada_embedding import get_ada_embedding
from store_task_results import store_task_results

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
openai.api_key = OPENAI_API_KEY

def execution_agent(objective:str, task: str):
    # Retrieve context for the task
    context = context_agent(task, "YOUR_TABLE_NAME", 5)

    # Generate prompt for OpenAI API
    prompt = f"{objective}. {task}. {context}"

    # Call OpenAI API to generate result
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )

    # Extract result from response
    result = response.choices[0].text.strip()

    # Store result in Pinecone
    store_task_results(task, result)

    return result
```