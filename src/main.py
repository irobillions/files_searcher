import datetime
import os
import textract

from search.search_base import SearchStrategy
from search.search_by_keyword import SearchByKeywordStrategy
from search.search_by_name import SearchByNameStrategy
from search.search_by_type import SearchByTypeStrategy
from search.search_by_metadata import SearchByMetadataStrategy
from utils.file_utils import *

class Main:
    def __init__(self, search_obj: SearchStrategy = SearchByNameStrategy(), logs=None):
        self.logs = logs
        self.searcher = search_obj

    @property
    def searcher(self):
        return self.searcher

    def process_menu(self):
        print("Choisissez le type de recherche :")
        print("1. Par nom de fichier")
        print("2. Par type de fichier (extension)")
        print("3. Par date ou période")
        print("4. Avec un mot dans son contenu")

        choice = input("Entrez le numéro correspondant à votre choix: ")

        if choice == '1':
            self.searcher = SearchByNameStrategy()
        elif choice == '2':
            self.searcher = SearchByTypeStrategy()
        elif choice == '3':
            self.searcher = SearchByMetadataStrategy()
        elif choice == '4':
            self.searcher  = SearchByKeywordStrategy()
        else:
            print("Choix invalide. Veuillez réessayer.")
            return self.process_menu()

    def run(self):
        self.process_menu()
        directories_list = get_directories()
        only_file = get_boolean_input("Uniquement des fichiers ? (oui/non): ")
        search_target = get_filename()

        results = self.searcher.search(directories_list, search_target)

        if only_file:
            results = [record for record in results if record["type"] != "Repertoire"]

        return results

    @searcher.setter
    def searcher(self, value):
        self._searcher = value


if __name__ == "__main__":
    # app = Main()
    # res = app.run()
    #
    # print(res)

    s = SearchByKeywordStrategy()

    directories = [r"D:\Ecole Polytechnique de Montreal\Sessions\H2023\INF1500\cours"]
    ##path_test = r"D:\Ecole Polytechnique de Montreal\Sessions\H2023\INF1500\cours\cours 1\cours_01.pptx"
    target = "Boole"
    # print(res)
    ##print(file_contain_keyword_pptx(path_test, target))
    res = s.search(directories, target)

    for element in res:
       print(element)


    # searcher = SearchByMetadataStrategy()
    # directories = ['D:\Ecole Polytechnique de Montreal']
    # search_target = { "target month": 6 , "target year": 2024,"end search date": '2024-07-1', 'keyword': 'CONSTANTES'}
    # res = searcher.search(directories, search_target)
    # # path = "D:\Ecole Polytechnique de Montreal\Sessions\A2022\INF1040\Q2_Q3-Analyse et investigation du problème.ppt"
    # # keyword = "l’essuie-glace"
    # # print(file_contain_keyword_ppt(path, keyword))
    #
    # print(res)


