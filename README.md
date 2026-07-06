#  LittleMongo AI

AI-powered document question answering system built using Retrieval-Augmented Generation (RAG).

## Features

- PDF document ingestion
- Semantic chunking
- FAISS vector database
- Sentence Transformers embeddings
- Google Gemini integration
- Streamlit interface

## Tech Stack

- Python
- FAISS
- Sentence Transformers
- Google Gemini
- Streamlit

## Architecture

PDF
↓

Chunking

↓

Embeddings

↓

FAISS

↓

Retriever

↓

Gemini

↓

Answer

## Installation

pip install -r requirements.txt

streamlit run streamlit_app.py