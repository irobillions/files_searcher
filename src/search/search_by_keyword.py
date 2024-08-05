import os
import threading
from abc import ABC

import pythoncom

from .files_infos import FileInfos
from .search_base import SearchStrategy
from .search_by_type import SearchByTypeStrategy
from utils.file_utils import *
class SearchByKeywordStrategy(SearchStrategy):
    def __init__(self, search_strategy: SearchStrategy = None):
        self.search_strategy = search_strategy
    def search(self, directories: list, search_target):
        results_path =[]
        try:
            def search_process():
                #comtypes.CoInitialize()
                for directory in directories:
                    for root, _, files in os.walk(directory):
                        for file in files:
                            _, extension = os.path.splitext(file)
                            if extension[1:] in ['txt', 'pptx', 'doc', 'docx', 'ppt', 'xls', 'xlsx', 'vsd', 'vsdx', 'txt', 'pdf']:
                                results_path.extend( self.search_content_strategy(extension[1:], os.path.join(root, file), search_target))
                            else:
                                pass

            thread = threading.Thread(target=search_process)
            thread.start()
            thread.join()
            return  results_path

        except Exception as e:
            print(f"Error in search keyword: {e}")

    @staticmethod
    def search_content_strategy(ext, file, search_target):
        results_path = []
        def search_keyword_process():
            if ext == 'txt':
                if file_contains_keyword_txt(file, search_target):
                    results_path.append(file)
            elif ext == 'pdf':
                if file_contain_keyword_pdf(file, search_target):
                    results_path.append(file)
            elif ext == 'doc' or ext == 'docx':
                if process_word_doc(ext, file, search_target):
                    results_path.append(file)
            elif ext == 'xlsx' or ext == 'xls':
                if process_excel_doc(ext, file, search_target):
                    results_path.append(file)
            elif ext == 'pptx' or ext == 'ppt':
                if process_powerpoint_doc(ext, file, search_target):
                    results_path.append(file)
            elif ext == 'vsd' or ext == 'vsdx':
                if file_contain_keyword_visio(file, search_target):
                    results_path.append(file)

        thread = threading.Thread(target=search_keyword_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_type = "Repertoire" if os.path.isdir(path) else "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results


class SearchKeywordTxtStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results_path = []
        searcher = SearchByTypeStrategy()
        def search_process():
           txt_files = searcher.search(directories, "txt")
           for file in txt_files:
                if file_contains_keyword_txt(file['path'], search_target):
                    results_path.append(file['path'])

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_type = "Repertoire" if os.path.isdir(path) else "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results



class SearchKeywordExcelStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results_path = []
        searcher = SearchByTypeStrategy()
        def search_process():
            xlsx_files = searcher.search(directories, "xlsx")
            xls_files = searcher.search(directories, "xls")
            excel_files = xls_files + xlsx_files

            for file in excel_files:
                _, extension = os.path.splitext(file.get('path'))
                if  process_excel_doc(extension[1:], file['path'], search_target):
                    results_path.append(file['path'])

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_type = "Repertoire" if os.path.isdir(path) else "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results

class SearchKeywordWordStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results_path = []
        searcher = SearchByTypeStrategy()
        def search_process():
            docx_files = searcher.search(directories, "docx")
            doc_files = searcher.search(directories, "doc")
            word_files = docx_files + doc_files

            for file in word_files:
                _, extension = os.path.splitext(file.get('path'))
                if process_word_doc(extension[1:], file['path'], search_target):
                    results_path.append(file['path'])

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_type = "Repertoire" if os.path.isdir(path) else "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results

class SearchKeywordPdfStrategy(SearchStrategy):

    def search(self, directories: list, search_target):
        results_path = []
        searcher = SearchByTypeStrategy()
        def search_process():
            pdf_files = searcher.search(directories, "pdf")

            for file in pdf_files:
                print("christ", file)
                if file_contain_keyword_pdf(file['path'], search_target):
                    results_path.append(file['path'])

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_type = "Repertoire" if os.path.isdir(path) else "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results



class SearchKeywordCsvStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        def search_process():
            pass


class SearchKeywordPowerPointStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results_path = []
        searcher = SearchByTypeStrategy()
        def search_process():
            pptx_files = searcher.search(directories, "pptx")
            ppt_files = searcher.search(directories, "ppt")
            powerpoint_files = pptx_files + ppt_files

            for file in powerpoint_files:
                _, extension = os.path.splitext(file.get('path'))
                if process_word_doc(extension[1:], file['path'], search_target):
                    results_path.append(file['path'])

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_type = "Repertoire" if os.path.isdir(path) else "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results


class SearchKeywordVisionStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results_path = []
        searcher = SearchByTypeStrategy()
        def search_process():
            vsdx_files = searcher.search(directories, "vsdx")
            vsd_files = searcher.search(directories, "vsd")
            visio_files = vsdx_files + vsd_files

            for file in visio_files:
                if file_contain_keyword_visio(file['path'], search_target):
                    results_path.append(file['path'])

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_type = "Repertoire" if os.path.isdir(path) else "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results