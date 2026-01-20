from abc import ABC, abstractmethod

class BaseLLM(ABC):
    @abstractmethod
    def summarize(self, text: str) -> str:
        pass

    @abstractmethod
    def explain_error(self, text: str) -> str:
        pass
