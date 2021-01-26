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

        self.assertTrue(np.allclose(np.array([0, 1]), searcher.documents))
        self.assertFalse(np.allclose(np.array([1, 0]), searcher.documents))

    def test_find_closest(self):
        searcher = SimilaritySearcher(TestEngine)
        searcher.add_document(Document(id=1, content='this is a content'))
        searcher.add_document(Document(id=2, content='this is another content'))

        text = 'this content' ## should be closest to "this is a content" because it does not have "another" into its words
        expected_id = searcher.get_closest([text], 1)
        self.assertEquals(expected_id, [1])

    def test_given_a_document_find_the_closest(self):
        searcher = SimilaritySearcher(TestEngine)
        searcher.add_document(Document(id=1, content='this is a content'))
        searcher.add_document(Document(id=2, content='this is another content'))

        result = searcher.get_closest_doc([2], 1)
        self.assertEquals(result, [2])

