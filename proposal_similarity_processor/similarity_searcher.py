from proposal_similarity_processor.document import Document


class SimilaritySearcher():
    def __init__(self) -> None:
        self.documents: [Document] = []

    def add_document(self, document: Document) -> None:
        self.documents.append(document)

