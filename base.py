from abc import ABC, abstractmethod

class Analyzer(ABC):
    """Базовый класс для всех анализов."""
    @abstractmethod
    def run(self, path: str) -> dict: 
        pass

class Exporter(ABC):
    """Базовый класс для сохранения результата анализа."""
    @abstractmethod
    def save(self, data: dict, filename: str):
        pass
