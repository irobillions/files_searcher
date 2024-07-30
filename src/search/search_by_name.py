import threading

from .search_base import SearchBase
from .files_infos import FileInfos
import os


class SearchByName(SearchBase):
    def __init__(self, directories: list, filename):
        super().__init__(directories)
        self.filename = filename

    def search(self):
        results_path = []

        def search_process():
            for directory in self.directories:
                for root, dirs, files in os.walk(directory):
                    for dir_name in dirs:
                        if self.filename.lower() in dir_name.lower():
                            path = os.path.join(root, dir_name)
                            results_path.append(path)

                    for file in files:
                        if self.filename.lower() in file.lower():
                            path = os.path.join(root, file)
                            results_path.append(path)

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        results = []

        for path in results_path:

            type = "Repertoire" if os.path.isdir(path) else "Fichier"

            file_infos = FileInfos(os.path.basename(path), path, type, "")
            file_infos.summarize()
            results.append(file_infos.to_dict())

        return results
