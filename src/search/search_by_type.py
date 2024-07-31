import glob
import os
import threading

from .files_infos import FileInfos
from .search_base import  SearchStrategy


class SearchByTypeStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results_path = []
        def search_process():
            for directory in directories:
                pattern = f"{directory}/**/*.{search_target}"
                path = glob.glob(pattern, recursive=True)
                results_path.extend(path)

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []
        for path in results_path:
            file_name, extension = os.path.splitext(path)
            if search_target.lower() == extension[1:].lower():
                file_type = "Fichier"
                file_infos = FileInfos(os.path.basename(path), path, file_type, "")
                results.append(file_infos.to_dict())

        return results
