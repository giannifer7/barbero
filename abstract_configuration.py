"""
Define the interface for a Configuration.
"""

from abc import ABC, abstractmethod
from abstract_browser import AbstractBrowser
import logging


class AbstractConfiguration:
    @property
    @abstractmethod
    def logger(self) -> logging.Logger:
        ...

    @property
    @abstractmethod
    def work_dir(self) -> str:
        ...

    @property
    @abstractmethod
    def browsers(self) -> dict[str, AbstractBrowser]:
        ...

    @abstractmethod
    def debug(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def info(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def warning(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def error(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def critical(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def work_path(self, f) -> str:
        ...
