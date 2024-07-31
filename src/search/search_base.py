from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, directories: list, search_target):
        raise NotImplemented("SearchStrategy has not been implemented yet.")