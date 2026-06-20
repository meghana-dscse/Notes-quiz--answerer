import os

import chromadb
import google.generativeai as genai

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

llm = genai.GenerativeModel(
    "gemini-2.5-flash"
)

client = chromadb.PersistentClient(
    path="vector_db"
)

collection = client.get_collection(
    name="notes"
)


def retrieve(query, history="", n_results=5):

    query_embedding = embedding_model.encode(
        query
    )

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results


def augment(query, history, results):

    retrieved_chunks = results["documents"][0]

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a helpful study assistant.

Use the previous conversation when relevant.

If the answer is not present in the context,
say so clearly.

Previous Conversation:

{history}

Context:

{context}

Question:

{query}

Answer:
"""

    return prompt


def generate(prompt):

    response = llm.generate_content(prompt)

    return response.text


def rag(query, history=""):

    results = retrieve(
        query,
        history
    )

    prompt = augment(
        query,
        history,
        results
    )

    answer = generate(prompt)

    sources = []

    for metadata in results["metadatas"][0]:

        source = metadata["source"]

        if source not in sources:
            sources.append(source)

    return answer, sources
