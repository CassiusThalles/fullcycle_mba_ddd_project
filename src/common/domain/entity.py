from abc import ABC, abstractmethod
class Entity(ABC):
    @abstractmethod
    def to_json(self) -> str:
        pass