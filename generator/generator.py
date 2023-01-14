from abc import ABC, abstractmethod
from blueprint import Blueprint


class Generator(ABC):
    """Base class for code generators
    """
    def __init__(self, path_to_generate) -> None:
        self.path_to_generate = path_to_generate

    @abstractmethod
    def generate(self, blueprint: Blueprint):
        """Generate code based on blueprint

        Args:
            blueprint (Blueprint): blueprint object used to generate state machine code.
        """
        pass
