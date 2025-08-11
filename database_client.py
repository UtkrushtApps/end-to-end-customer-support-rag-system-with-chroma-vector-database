from typing import Any, Dict, Optional

class ChromaDBClient:
    """
    Basic client for connecting to Chroma DB service on localhost:8000
    """
    def __init__(self, config: Dict[str, Any]):
        pass

    def create_collection(self, name: str, dimension: int, metric: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """
        Create a collection in the database with specified dimension and similarity metric.
        Args:
            name: name of the collection
            dimension: embedding dimension
            metric: similarity metric (e.g. 'cosine', 'dotproduct')
            metadata: collection schema or description (optional)
        """
        pass

    def insert_embeddings(self, collection_name: str, embeddings: list, metadatas: list) -> None:
        """
        Batch insert vectors and associated metadata into the collection.
        Args:
            collection_name: target collection name
            embeddings: list of embedding vectors
            metadatas: list of dicts with metadata details
        """
        pass

    def query(self, collection_name: str, query_vector: Any, top_k: int = 5) -> list:
        """
        Query vectors in the specified collection for the k most similar results.
        Args:
            collection_name: name of the collection
            query_vector: embedding of the query text
            top_k: number of top results to return
        Returns:
            List of result metadata and content
        """
        pass
