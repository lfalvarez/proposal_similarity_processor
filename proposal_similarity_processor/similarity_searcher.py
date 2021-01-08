from proposal_similarity_processor.document import Document
from scipy.spatial.distance import cdist
import numpy as np

class SimilaritySearcher():
    def __init__(self, search_engine_class: type, distance_type: str = 'euclidean') -> None:
        self.distance_type = distance_type
        self.documents = []
        self.search_engine = search_engine_class()
        self.index_document_id_relations = {}
        self.document_id_index_relations = {}

    def add_document(self, document: Document) -> None:
        next_index = len(self.documents)
        document_index = document.id
        self.documents.append(self.search_engine.vectorize(document.content))
        self.index_document_id_relations[next_index] = document_index
        self.document_id_index_relations[str(document_index)] = next_index

    def find_nearest(self, value: [int], k:int) -> [int]:
        docs = np.asarray(self.documents)
        distances = cdist(docs, np.atleast_2d(value), self.distance_type).transpose()
        return np.argpartition(distances, k)[0]

    def get_closest(self, text:str, k:int):
        vectorized_input = self.search_engine.vectorize(text)
        index = self.find_nearest(vectorized_input, k)
        closest_element_indexes = np.asarray(index)
        indexes = []
        for index in closest_element_indexes:
            indexes.append(self.index_document_id_relations[index])
        return indexes[0:k]

    def get_closest_doc(self, id:int, k: int):
        document_index_position = self.document_id_index_relations[str(id)]
        vectorized_input = self.documents[document_index_position]
        closest_indexes = self.find_nearest(vectorized_input, k)
        doc_ids = []
        for index in closest_indexes:
            doc_ids.append(self.index_document_id_relations[index])
        return doc_ids[0:k]
