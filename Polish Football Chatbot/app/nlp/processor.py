from abc import ABC, abstractmethod

class NLPProcessor(ABC):
    """
    Abstract base class for NLP processors.
    This demonstrates the Strategy design pattern.
    """
    @abstractmethod
    def process(self, text):
        """
        Process the input text to determine the user's intent.

        :param text: The user's input text.
        :return: The identified intent.
        """
        pass
