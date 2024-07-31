import threading

from .search_base import SearchStrategy
from .files_infos import FileInfos
import os

class SearchByNameStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        results_path = []
        def search_process():
            for directory in directories:
                for root, dirs, files in os.walk(directory):
                    for dir_name in dirs:
                        if search_target.lower() in dir_name.lower():
                            path = os.path.join(root, dir_name)
                            results_path.append(path)

                    for file in files:
                        if search_target.lower() in file.lower():
                            path = os.path.join(root, file)
                            results_path.append(path)

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
