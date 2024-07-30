class FileInfos:
    def __init__(self, name, path, type, abstract=None):
        self.name = name
        self.path = path
        self.type = type
        self.abstract = abstract

    def __str__(self):
        return f"__File Information__\n " \
               f"filename: {self.name}\n " \
               f"path: {self.path}\n " \
               f"type: {self.type}\n " \
               f"resume: {self.abstract}"

    def to_dict(self):
        return {
                    "filename": self.name,
                    "path": self.path,
                    "type": self.type,
                    "abstract": self.abstract
                }

    def summarize(self, function=None):
        pass
        ##raise NotImplemented("Subclass should implement this method")
