from typing import List, Dict, Any

def load_support_documents(document_dir: str) -> List[Dict[str, Any]]:
    """
    Load and parse all support documents from a directory.
    Args:
        document_dir: path to support files
    Returns:
        List of dicts with document content and metadata
    """
    pass

def preprocess_and_clean(text: str) -> str:
    """
    Preprocess and clean the document text (removal of junk, normalization, deduplication).
    Args:
        text: raw document text
    Returns:
        Cleaned text string
    """
    pass

def chunk_with_overlap(cleaned_text: str, chunk_size: int, overlap: int) -> List[str]:
    """
    Divide cleaned text into overlapping chunks.
    Args:
        cleaned_text: cleaned support text
        chunk_size: length of each chunk (in characters/tokens)
        overlap: number of characters/tokens to overlap
    Returns:
        List of chunk strings
    """
    pass

def attach_chunk_metadata(chunk: str, document_metadata: Dict[str, Any], chunk_index: int) -> Dict[str, Any]:
    """
    Attach metadata to a chunk including reference to source document and location.
    Args:
        chunk: text chunk
        document_metadata: original doc metadata
        chunk_index: index of this chunk in the doc
    Returns:
        Metadata dictionary for storage
    """
    pass
