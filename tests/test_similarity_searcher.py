from unittest import TestCase

from proposal_similarity_processor.document import Document
from proposal_similarity_processor.similarity_searcher import SimilaritySearcher


class SimilaritySearcherTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_instantiate_and_add_document(self):
        searcher = SimilaritySearcher()
        searcher.add_document(Document(id=1, content='this is a content'))
        searcher.add_document(Document(id=2, content='this is another content'))

        self.assertEqual(2, len(searcher.documents))

