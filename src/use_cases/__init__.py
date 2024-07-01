from abc import ABC, abstractmethod
from src.dtos import Dtos

class UseCase(ABC):
    @abstractmethod
    def execute(self, command: Dtos):
        pass