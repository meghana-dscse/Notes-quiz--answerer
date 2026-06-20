# StudyMate AI

StudyMate AI is a Retrieval-Augmented Generation (RAG) based study assistant designed to answer questions directly from academic notes and learning materials. The system processes PDFs, PowerPoint presentations, Word documents, and text files, converts them into searchable knowledge, and generates context-aware answers grounded in the uploaded content.

The objective of this project is to transform static study resources into an interactive learning assistant capable of retrieving relevant information, maintaining conversational context, and providing source-backed responses.

## Features

* Multi-format document ingestion

  * PDF
  * DOCX
  * PPTX
  * TXT

* Automated document processing

  * Parsing
  * Cleaning
  * Chunking
  * Embedding generation

* Semantic search using vector similarity

* Conversational question answering

* Source-grounded responses

* Session-based memory for follow-up questions

* Web-based chat interface

* Hallucination-aware responses that prioritize information available in the knowledge base

## System Workflow

1. Documents are collected from the knowledge base.
2. Text is extracted from supported file formats.
3. Content is cleaned and normalized.
4. Documents are split into semantic chunks.
5. Embeddings are generated using a Sentence Transformer model.
6. Embeddings are stored in ChromaDB.
7. User queries are converted into embeddings.
8. Relevant chunks are retrieved from the vector database.
9. Retrieved context is combined with conversation history.
10. Gemini generates a response grounded in the retrieved information.
11. Sources used for answering are displayed alongside the response.

## Architecture

User Query

↓

Retrieval

↓

ChromaDB Vector Store

↓

Relevant Chunks

↓

Context Augmentation

↓

Gemini Generation

↓

Grounded Response + Sources

## Technology Stack

### Backend

* Python
* Flask

### Document Processing

* PyPDF
* python-docx
* python-pptx

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* ChromaDB

### Large Language Model

* Gemini 2.5 Flash

### Frontend

* HTML
* CSS
* JavaScript

## Project Structure

```text
StudyMate-AI/
│
├── app.py
├── requirements.txt
├── src/
│   └── rag.py
│
├── templates/
│   └── index.html
│
├── notebooks/
│   ├── loading.ipynb
│   ├── cleaning.ipynb
│   ├── chunks.ipynb
│   ├── embeddings.ipynb
│   ├── storage.ipynb
│   └── RAG.ipynb
│
├── vector_db/
│
└── .gitignore
```

## Key Components

### Data Ingestion

The ingestion pipeline supports multiple document formats and extracts textual content into a unified structure for downstream processing.

### Data Cleaning

Extracted text is normalized and prepared for chunking while preserving important learning content.

### Chunking

Large documents are divided into manageable semantic chunks to improve retrieval accuracy and reduce context noise.

### Embedding Generation

Each chunk is converted into a dense vector representation using a transformer-based embedding model.

### Vector Storage

Embeddings and metadata are stored inside ChromaDB for efficient similarity search.

### Retrieval

Relevant chunks are retrieved using semantic similarity between the user query and stored embeddings.

### Context Augmentation

Retrieved information is combined with conversational history to provide context-aware responses.

### Generation

Gemini generates answers strictly based on the retrieved content, helping reduce hallucinations and improve reliability.

## Example Capabilities

* Explain concepts from lecture notes
* Summarize uploaded study material
* Answer follow-up questions using conversational context
* Retrieve information from multiple documents
* Provide source references for generated answers
* Act as a subject-specific learning assistant

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

Start the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Design Philosophy

The project focuses on understanding and implementing the complete RAG lifecycle rather than relying on high-level frameworks. Every stage of the pipeline, from ingestion and chunking to retrieval and generation, is explicitly built and integrated to provide a deeper understanding of modern AI application architecture.

The interface was rapidly prototyped and refined using modern AI-assisted development workflows, while the retrieval pipeline, vector storage architecture, conversational memory, and backend orchestration were designed and implemented as part of the project.

## Future Improvements

* User document uploads through the interface
* Persistent multi-session memory
* Retrieval re-ranking
* Hybrid search
* Evaluation metrics for retrieval quality
* Cloud deployment and scaling
* Multi-user support
* Advanced citation and source visualization

## Author

Gadi Meghana

Built to explore modern Retrieval-Augmented Generation systems, semantic search, conversational AI, and production-oriented AI application development.
