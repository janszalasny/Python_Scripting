"""
Keyword Generator Core Logic.

This module contains the core classes for the keyword generator, including:
- KeywordGenerator: The main class that generates keywords.
- StrategyFactory: A factory for creating keyword generation strategies.
"""

from typing import List
import pandas as pd
from .strategies import (
    KeywordGenerationStrategy,
    BroadMatchStrategy,
    PhraseMatchStrategy,
    ExactMatchStrategy
)
from .observers import KeywordSaver


class KeywordGenerator:
    """
    The main class for generating AdWords keywords.

    This class uses the Strategy pattern to allow for different keyword
    generation methods (e.g., broad match, phrase match, exact match).
    It also uses the Observer pattern to notify observers when new
    keywords are generated.
    """

    def __init__(self, products: List[str], modifiers: List[str]):
        self.products = products
        self.modifiers = modifiers
        self._strategy: KeywordGenerationStrategy | None = None
        self._observers: List[KeywordSaver] = []

    def attach(self, observer: KeywordSaver):
        """Attach an observer to the keyword generator."""
        self._observers.append(observer)

    def detach(self, observer: KeywordSaver):
        """Detach an observer from the keyword generator."""
        self._observers.remove(observer)

    def notify(self, keywords: pd.DataFrame):
        """Notify all observers about newly generated keywords."""
        for observer in self._observers:
            observer.update(keywords)

    def set_strategy(self, strategy: KeywordGenerationStrategy):
        """Set the keyword generation strategy."""
        self._strategy = strategy

    def generate_keywords(self):
        """
        Generate keywords using the current strategy and notify observers.
        """
        if not self._strategy:
            raise ValueError("Keyword generation strategy not set.")

        generated_keywords = self._strategy.generate(self.products, self.modifiers)
        self.notify(generated_keywords)


class StrategyFactory:
    """
    A factory for creating keyword generation strategies.
    """

    def create_strategy(self, strategy_type: str) -> KeywordGenerationStrategy:
        """
        Create a keyword generation strategy based on the given type.

        Args:
            strategy_type: The type of strategy to create ('broad', 'phrase', 'exact').

        Returns:
            A KeywordGenerationStrategy instance.
        """
        if strategy_type == 'broad':
            return BroadMatchStrategy()
        if strategy_type == 'phrase':
            return PhraseMatchStrategy()
        if strategy_type == 'exact':
            return ExactMatchStrategy()
        raise ValueError(f"Unknown strategy type: {strategy_type}")
