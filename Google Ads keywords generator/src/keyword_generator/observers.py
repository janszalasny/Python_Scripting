"""
Keyword Savers (Observers).

This module contains the observer classes that are responsible for saving
the generated keywords to different destinations (e.g., CSV, console).
"""

from abc import ABC, abstractmethod
import pandas as pd
import os


class KeywordSaver(ABC):
    """
    Abstract base class for a keyword saver (observer).
    """

    @abstractmethod
    def update(self, keywords: pd.DataFrame):
        """
        Receive an update with newly generated keywords.

        Args:
            keywords: A pandas DataFrame with the generated keywords.
        """
        pass


class CsvKeywordSaver(KeywordSaver):
    """
    A keyword saver that saves the keywords to a CSV file.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        # Ensure the directory for the output file exists.
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)

    def update(self, keywords: pd.DataFrame):
        """
        Save the generated keywords to a CSV file.

        Args:
            keywords: A pandas DataFrame with the generated keywords.
        """
        try:
            # Check if the file exists and is not empty to append with header correctly
            header = not os.path.exists(self.filepath)
            keywords.to_csv(self.filepath, mode='a', header=header, index=False)
            print(f"Keywords saved to {self.filepath}")
        except Exception as e:
            print(f"Error saving keywords to {self.filepath}: {e}")


class ConsoleKeywordSaver(KeywordSaver):
    """
    A keyword saver that prints the keywords to the console.
    """

    def update(self, keywords: pd.DataFrame):
        """
        Print the generated keywords to the console.

        Args:
            keywords: A pandas DataFrame with the generated keywords.
        """
        print("--- New Keywords Generated ---")
        print(keywords.to_string(index=False))
