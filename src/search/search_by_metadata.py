import os
import threading
from abc import ABC
from datetime import datetime

from search.files_infos import FileInfos
from search.search_base import SearchStrategy


class SearchByMetadataStrategy(SearchStrategy):
    def search(self, directories: list, search_target):
        matching_files = []
        def search_process():
            for directory in directories:
                for root, _, files in os.walk(directory):
                    for file in files:
                        path = os.path.join(root, file)
                        if len(search_target['keyword']) > 0:
                            if search_target.get('keyword') in os.path.basename(path):
                                file_infos = FileInfos(file, path, "Fichier", "")
                                if self.is_file_matching(file_infos, search_target):
                                    matching_files.append(file_infos.to_dict())
                        else:
                            file_infos = FileInfos(file, path, "Fichier", "")
                            if self.is_file_matching(file_infos, search_target):
                                matching_files.append(file_infos.to_dict())

        thread = threading.Thread(target=search_process)
        thread.start()
        thread.join()

        return matching_files


    @staticmethod
    def is_file_matching(file_infos, search_target):
        try:
            target_month = search_target.get('target month')
            target_year = search_target.get('target year')
            end_search_date = search_target.get('end search date')

            if target_month is None or target_year is None or end_search_date is None:
                return False

            end_date = datetime.strptime(end_search_date, '%Y-%m-%d')
            file_mod_time = datetime.strptime(file_infos.modification_time, '%a %b %d %H:%M:%S %Y')
            file_access_time = datetime.strptime(file_infos.access_time, '%a %b %d %H:%M:%S %Y')

            start_date = datetime(target_year, target_month, 1)
            if start_date <= file_mod_time <= end_date or start_date <= file_access_time <= end_date:
                return True

        except Exception as e:
            print(f"Erreur dans is_file_matching: {e}")

        return False