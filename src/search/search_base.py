from abc import ABC, abstractmethod


class SearchBase(ABC):
    def __int__(self, directories: list):
        self.directories = directories

    @abstractmethod
    def search(self):
        raise NotImplemented("subClass should implement this method")