from abc import ABC, abstractmethod
from Blueprint import Blueprint


class Generator(ABC):
    """Base class for code generators
    """
    @abstractmethod
    def generate(self, blueprint: Blueprint):
        """Generate code based on blueprint

        Args:
            blueprint (Blueprint): blueprint object used to generate state machine code.
        """
        pass
