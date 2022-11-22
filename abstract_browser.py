"""
Define the interface for a Browser.
"""

from abc import ABC, abstractmethod


class AbstractBrowser(ABC):
    """Declare the interface for the Browser classes."""

    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the browser."""
        ...

    @property
    @abstractmethod
    def db_path(self) -> str:
        """The path of the sqlite database with the browser's history."""
        ...

    @property
    @abstractmethod
    def history_query(self) -> str:
        """A sqlite query for the browser's history."""
        ...
