from proposal_similarity_processor.document import Document


class SimilaritySearcher():
    def __init__(self, search_engine_class: type) -> None:
        self.documents = []
        self.search_engine = search_engine_class()

    def add_document(self, document: Document) -> None:
        self.documents.append(self.search_engine.vectorize(document.content))

