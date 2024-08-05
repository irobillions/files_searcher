import os
import time
from datetime import datetime

class FileInfos:
    def __init__(self, name, path, type, abstract=None):
        self.name = name
        self.path = path
        self.type = type
        self.abstract = abstract
        self.access_time = None
        self.creation_time = None
        self.modification_time = None
        self.get_metadata()

    def __str__(self):
        return f"__File Information__\n " \
               f"filename: {self.name}\n " \
               f"path: {self.path}\n " \
               f"type: {self.type}\n " \
               f"resume: {self.abstract}"

    def get_metadata(self):
        file_stats = os.stat(self.path)
        self.creation_time = time.ctime(file_stats.st_ctime)
        self.modification_time = time.ctime(file_stats.st_mtime)
        self.access_time = time.ctime(file_stats.st_atime)

    def to_dict(self):
        return {
                    "filename": self.name,
                    "path": self.path,
                    "type": self.type,
                    "abstract": self.abstract,
                    "access_time": self.access_time,
                    "creation_time": self.creation_time,
                    "modification_time": self.modification_time
                }

    def summarize(self, function=None):
        pass
        ##raise NotImplemented("Subclass should implement this method")
