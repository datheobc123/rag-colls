from rag_colls.core.base.retrievers.base import BaseRetriever
from rag_colls.core.base.database.bm25 import BaseBM25Retriever

from rag_colls.types.retriever import RetrieverQueryType, RetrieverResult


class BM25Retriever(BaseRetriever):
    """
    A retriever that uses BM25 to retrieve documents based on a query.
    """

    def __init__(self, bm25: BaseBM25Retriever):
        """
        Initialize the BM25Retriever class.

        Args:
            bm25: The BM25 retriever to use for retrieval.
            embed_model: The embedding model to use for generating embeddings.
        """
        self.bm25 = bm25

    @classmethod
    def from_bm25(cls, bm25: BaseBM25Retriever) -> "BM25Retriever":
        """
        Create an instance of BM25Retriever from a BM25 retriever.

        Args:
            bm25: The BM25 retriever to use for retrieval.

        Returns:
            BM25Retriever: An instance of the retriever.
        """
        return cls(bm25=bm25)

    def _retrieve(self, query: RetrieverQueryType, **kwargs) -> list[RetrieverResult]:
        """
        Retrieve documents based on the query.

        Args:
            query: The query to search for.
            **kwargs: Additional keyword arguments for the retrieval process.

        Returns:
            list[RetrieverResult]: A list of retrieved documents.
        """
        assert isinstance(query, str), "Query must be a string."

        return self.bm25.search(query=query, **kwargs)
