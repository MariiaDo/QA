from abc import ABC, abstractmethod


class Write(ABC):

    @abstractmethod
    def write(self, text: str):
        pass