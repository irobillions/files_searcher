import os
import textract


from search.search_by_type import SearchByTypeStrategy
from utils.file_utils import *


class Main:
    def __init__(self, logs=None):
        self.logs = logs
        self.searcher = None

    def run(self):
        directories = get_directories()
        only_file = get_boolean_input("Uniquement des fichiers ? (oui/non): ")
        pattern_to_search = get_filename()

        self.searcher = SearchByTypeStrategy()
        results = self.searcher.search(directories, pattern_to_search)

        if only_file:
            results = [record for record in results if record["type"] != "Repertoire"]

        return results


if __name__ == "__main__":
    # app = Main()
    # res = app.run()
    #
    # print(res)

    path = "D:\Ecole Polytechnique de Montreal\Sessions\A2022\MTH1101\Documents généraux\Plan-cours- A22.pdf"
    keyword = "MacLaurin"
    print(file_contain_keyword_pdf(path, keyword))


