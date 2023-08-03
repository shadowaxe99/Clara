```python
import openai

def get_ada_embedding(query):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    model = "text-davinci-002"
    response = openai.Completion.create(
      engine=model,
      prompt=query,
      max_tokens=64
    )
    return response['choices'][0]['text'].strip()
```