from abc import ABC

from search_base import SearchStrategy
class SearchByKeywordStrategy(SearchStrategy):
    def __init__(self, search_strategy: SearchStrategy):
        self.search_strategy = search_strategy
    def search(self, directories: list, search_target):
        return self.search_strategy.search(directories, search_target)

class SearchKeywordTxtStrategy(SearchStrategy):
    def search(self, directories: list, search_target):

        def search_process()
class SearchKeywordDocxStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results = []
        def search_process():
            pass



class SearchKeywordXlsxStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        def search_process():
            pass

class SearchKeywordDocStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        def search_process():
            pass


class SearchKeywordXlsStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        def search_process():
            pass
