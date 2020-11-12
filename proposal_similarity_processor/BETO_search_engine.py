import torch
from transformers import BertForMaskedLM, BertTokenizer

from proposal_similarity_processor.abstract_search_engine import AbstractSearchEngine


class BETOSearchEngine(AbstractSearchEngine):
    def __init__(self):
        super().__init__()
        self.tokenizer = BertTokenizer.from_pretrained("pytorch/", do_lower_case=False)
        self.model = BertForMaskedLM.from_pretrained("pytorch/")

    def get_entire_phrase_vectorized(self, text):
        tokens = self.tokenizer.tokenize(text)
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokens)
        tokens_tensor = torch.tensor([indexed_tokens])
        predictions = self.model(tokens_tensor)[0]
        return predictions

    def vectorize(self, text):
        all_words = self.get_entire_phrase_vectorized(text)
        return all_words[0].mean(0).detach().numpy()
