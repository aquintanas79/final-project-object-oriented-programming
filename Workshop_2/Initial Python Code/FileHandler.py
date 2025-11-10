from abc import ABC, abstractmethod
import json

class FileHandler(ABC):
    @abstractmethod
    def read(self, path):
        pass

    @abstractmethod
    def write(self, path, data):
        pass

class JsonFileHandler(FileHandler):
    def read(self, path):
        with open(path, "r") as file:
            return json.load(file)

    def write(self, path, data):
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
