from search_base import  SearchBase



class SearchByType(SearchBase):
    def __init__(self, filetype, directories: list):
        super().__init__(directories)
        self.filetype = filetype


    def search(self):
        results_path = []
        def search_process():




