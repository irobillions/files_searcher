import os

from search.search_by_name import SearchByName
from utils.file_utils import *


class Main:
    def __init__(self, logs=None):
        self.logs = logs
        self.searcher = None

    def run(self):
        directories = get_directories()
        only_file = get_boolean_input("Uniquement des fichiers ? (oui/non): ")
        filename_to_search = get_filename()

        self.searcher = SearchByName(directories, filename_to_search)
        results = self.searcher.search()

        if only_file:
            results = [record for record in results if record["type"] != "Repertoire"]

        return results


if __name__ == "__main__":
    app = Main()
    res = app.run()

    print(res)
