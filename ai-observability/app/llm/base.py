from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def summarize(self, text: str) -> str:
        pass

    @abstractmethod
    def explain_error(self, text: str) -> str:
        pass
