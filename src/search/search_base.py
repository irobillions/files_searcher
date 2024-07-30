from abc import ABC, abstractmethod


class SearchBase(ABC):
    def __init__(self, directories: list):
        self.directories = directories

    @abstractmethod
    def search(self):
        raise NotImplemented("subclass should implement this method")