from unittest import TestCase

from proposal_similarity_processor.abstract_search_engine import AbstractSearchEngine
from proposal_similarity_processor.document import Document
from proposal_similarity_processor.similarity_searcher import SimilaritySearcher
import numpy as np


class TestEngine(AbstractSearchEngine):
    def __init__(self):
        super().__init__()

    def vectorize(self, text):
        if 'another' in text:
            return np.array([1, 0])
        return np.array([0, 1])


class SimilaritySearcherTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_instantiate_and_add_document(self):
        searcher = SimilaritySearcher(TestEngine)
        searcher.add_document(Document(id=1, content='this is a content'))
        searcher.add_document(Document(id=2, content='this is another content'))

        self.assertEqual(2, len(searcher.documents))

    def test_it_vectorizes_documents(self):
        searcher = SimilaritySearcher(TestEngine)
        searcher.add_document(Document(id=1, content='this is a content'))

        self.assertTrue(np.allclose(np.array([0,1]), searcher.documents))
        self.assertFalse(np.allclose(np.array([1, 0]), searcher.documents))
