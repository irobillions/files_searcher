from abc import  ABC, abstractmethod


class BaseSummarizer(ABC):
    def __init__(self, type="txt"):
        self.type = type

    @abstractmethod
    def summarize(self):
        raise NotImplemented("Must implement this")
