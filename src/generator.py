import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question, docs):

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI assistant that answers ONLY using the provided MongoDB documentation.

Context:
{context}

Question:
{question}

Give a clear, concise answer.
"""

    response = model.generate_content(prompt)

    return response.text