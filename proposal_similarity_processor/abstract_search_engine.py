from abc import ABC, abstractmethod


class AbstractSearchEngine(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def vectorize(self, text):
        raise NotImplemented


