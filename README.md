# Customer Support RAG System Task

## Task Overview
You will build, from scratch, a complete question-answering system based on Retrieval-Augmented Generation (RAG) for a fictional tech startup's customer support team. Your goal is to process company support materials (FAQs, troubleshooting guides, product manuals), store their embeddings in a Chroma vector database, and enable semantic retrieval and generation of accurate support answers. All core logic—in document handling, chunking, embedding, database integration, retrieval, and prompt-based response generation—must be implemented by you using the provided minimal infrastructure.

## Guidance
- Source or create realistic customer-facing documents and place them in `data/documents/`.
- Implement your own pipelines for:
  - Parsing, cleaning, and de-duplicating support documents
  - Chunking content with overlap and attaching metadata (title, section, source, etc.)
  - Generating embeddings for all chunks using an embedding model of your choice
  - Configuring and populating a Chroma collection for efficient, idempotent batch upserts
  - Implementing retrieval logic using vector similarity (cosine or dot-product) and tuning top-k
  - Creating a context assembly mechanism to prepare relevant context for answer generation
  - Designing prompts for accurate, helpful, and cited support responses
  - Logging and evaluating recall@k, precision@k, and query latency per query
- You may use any pipelines, frameworks, or libraries you find appropriate as long as final code integrates with the existing project structure and the Chroma DB at localhost:8000.
- Infrastructure (database and connection code) is pre-configured—do not modify the setup scripts or database deployment.

## Database Access Information
- Chroma DB service is running at http://localhost:8000, accessible from your host environment.
- Create and configure your own Chroma collection(s) with dimension and metric that match your embeddings.
- Batch insert or upsert embeddings and metadata—ensure schema consistency and efficient ingestion.
- Validate your database with retrieval tests (see `sample_queries.txt` for sample questions).

## Objectives
- Implement document ingestion, chunking, metadata, and deduplication for diverse support content
- Select and apply an embedding approach suitable for customer support knowledge
- Store and manage all data efficiently in Chroma DB with clear, reproducible ingestion scripts
- Build end-to-end semantic retrieval and response generation pipelines, including prompts that ensure useful answers with citations
- Log, evaluate, and tune your system for accuracy (recall@k, precision@k) and latency
- Deliver a working RAG pipeline that handles realistic queries and delivers high-quality answers

## How To Verify
- Confirm correct chunking, metadata, and embedding generation for your source documents
- Insert vectors and metadata into your configured Chroma collection, validating inserts with a few batch retrievals
- Issue sample support queries and observe both relevant context retrieval and high-quality answer generation with source citations
- Review your evaluation logs for recall@k and precision@k against candidate answers
- Check for response latency and tune retrieval hyperparameters as needed
