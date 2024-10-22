import time
import openai
from langchain_community.vectorstores import FAISS

def create_embeddings(openai_api_key, input_text, retries=5, backoff_factor=1):
    # Initialize OpenAI with your API key
    openai.api_key = openai_api_key
    for attempt in range(retries):
        try:
            # Create embeddings for the input text
            response = openai.Embedding.create(
                input=input_text,
                model="text-embedding-ada-002"
            )
            return response['data']
        except openai.error.RateLimitError as e:
            print(f"Rate limit error: {e}")
            wait_time = backoff_factor * (2 ** attempt)  # Exponential backoff
            print(f"Retrying in {wait_time} seconds...")
            time.sleep(wait_time)  # Wait before retrying
    raise Exception("Maximum retries exceeded for creating embeddings.")

def create_vector_store(texts, openai_api_key):
    embeddings = []
    for text in texts:
        embedding = create_embeddings(openai_api_key, text)  # Pass the API key here
        embeddings.append(embedding)

    # Create the vector store with the embeddings
    vector_store = FAISS.from_texts(texts, embeddings)
    return vector_store
