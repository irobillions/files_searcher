class FileInfos:
    def __init__(self, name, path, abstract=None):
        self.name = name
        self.path = path
        self.abstract = abstract

    def __str__(self):
        return f"__File Information__\n " \
               f"filename: {self.name}\n " \
               f"path: {self.path}\n " \
               f"resume: {self.abstract}"

    def to_dict(self):
        return {"filename": self.name,
                "path": self.path,
                "abstract": self.abstract
                }

    def summarize(self, function=None):
        raise NotImplemented("Subclass should implement this method")
