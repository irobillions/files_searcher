import glob
import os
import threading

from .files_infos import FileInfos
from .search_base import  SearchBase



class SearchByType(SearchBase):
    def __init__(self, type_pattern, directories: list):
        super().__init__(directories)
        self.type_pattern = type_pattern


    def search(self):
        results_path = []
        def search_process():

            for directory in self.directories:
                pattern = f"{directory}/**/*.{self.type_pattern}"
                path = glob.glob(pattern, recursive=True)
                results_path.extend(path)

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()
        results =[]

        for path in results_path:
            file_type = "Fichier"
            file_infos = FileInfos(os.path.basename(path), path, file_type, "")
            results.append(file_infos.to_dict())

        return results



