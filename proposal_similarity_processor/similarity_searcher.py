from proposal_similarity_processor.document import Document
from scipy.spatial.distance import cdist
import numpy as np

class SimilaritySearcher():
    def __init__(self, search_engine_class: type, distance_type: str = 'euclidean') -> None:
        self.distance_type = distance_type
        self.documents = []
        self.search_engine = search_engine_class()
        self.index_document_id_relations = {}

    def add_document(self, document: Document) -> None:
        next_index = len(self.documents)
        document_index = document.id
        self.documents.append(self.search_engine.vectorize(document.content))
        self.index_document_id_relations[next_index] = document_index

    def find_nearest(self, value):
        docs = np.asarray(self.documents)
        return cdist(docs, np.atleast_2d(value), self.distance_type).argmin()

    def get_closest(self, text):
        vectorized_input = self.search_engine.vectorize(text)
        index = self.find_nearest(vectorized_input)
        return self.index_document_id_relations[index]

