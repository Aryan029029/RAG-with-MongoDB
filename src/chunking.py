from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents,
                    chunk_size=500,
                    chunk_overlap=150):
    """
    Split documents into overlapping chunks.

    Args:
        documents: List of LangChain Document objects.
        chunk_size: Maximum number of tokens/characters per chunk.
        chunk_overlap: Number of overlapping tokens/characters.

    Returns:
        List of chunked documents.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks