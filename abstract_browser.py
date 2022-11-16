"""
Define the interface for a Browser.
"""

from abc import ABC, abstractmethod


class AbstractBrowser(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def db_path(self) -> str:
        ...

    @property
    @abstractmethod
    def history_query(self) -> str:
        ...
