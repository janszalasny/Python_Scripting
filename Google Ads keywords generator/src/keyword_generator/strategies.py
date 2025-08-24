"""
Keyword Generation Strategies.

This module contains the abstract base class for strategies and the
concrete implementations, including:
- KeywordGenerationStrategy: The abstract base class.
- BroadMatchStrategy: For generating broad match keywords.
- PhraseMatchStrategy: For generating phrase match keywords.
- ExactMatchStrategy: For generating exact match keywords.
"""

from abc import ABC, abstractmethod
from typing import List
import pandas as pd
from itertools import product


class KeywordGenerationStrategy(ABC):
    """
    Abstract base class for a keyword generation strategy.
    """

    @abstractmethod
    def generate(self, products: List[str], modifiers: List[str]) -> pd.DataFrame:
        """
        Generate keywords based on a given strategy.

        Args:
            products: A list of product keywords.
            modifiers: A list of modifier keywords.

        Returns:
            A pandas DataFrame with the generated keywords.
        """
        pass


class BroadMatchStrategy(KeywordGenerationStrategy):
    """
    A strategy for generating broad match keywords.
    """

    def generate(self, products: List[str], modifiers: List[str]) -> pd.DataFrame:
        """
        Generate broad match keywords by combining products and modifiers.

        Args:
            products: A list of product keywords.
            modifiers: A list of modifier keywords.

        Returns:
            A pandas DataFrame with the generated broad match keywords.
        """
        keywords = [f"{mod} {prod}" for mod, prod in product(modifiers, products)]
        return pd.DataFrame({'keyword': keywords, 'match_type': 'Broad'})


class PhraseMatchStrategy(KeywordGenerationStrategy):
    """
    A strategy for generating phrase match keywords.
    """

    def generate(self, products: List[str], modifiers: List[str]) -> pd.DataFrame:
        """
        Generate phrase match keywords by combining products and modifiers.

        Args:
            products: A list of product keywords.
            modifiers: A list of modifier keywords.

        Returns:
            A pandas DataFrame with the generated phrase match keywords.
        """
        keywords = [f'"{mod} {prod}"' for mod, prod in product(modifiers, products)]
        return pd.DataFrame({'keyword': keywords, 'match_type': 'Phrase'})


class ExactMatchStrategy(KeywordGenerationStrategy):
    """
    A strategy for generating exact match keywords.
    """

    def generate(self, products: List[str], modifiers: List[str]) -> pd.DataFrame:
        """
        Generate exact match keywords by combining products and modifiers.

        Args:
            products: A list of product keywords.
            modifiers: A list of modifier keywords.

        Returns:
            A pandas DataFrame with the generated exact match keywords.
        """
        keywords = [f'[{mod} {prod}]' for mod, prod in product(modifiers, products)]
        return pd.DataFrame({'keyword': keywords, 'match_type': 'Exact'})
