"""
Define the interface for a Configuration.
"""

import logging
from abc import ABC, abstractmethod

from abstract_browser import AbstractBrowser


class AbstractConfiguration(ABC):
    """Configuration and default logging interface,
    often the first argument of library functions.
    See https://en.wikipedia.org/wiki/Dependency_injection"""

    @property
    @abstractmethod
    def logger(self) -> logging.Logger:
        """A general logger. This keeps the functions that use it reentrant,
        as it's passed down the call stack with the configuration.
        Perhaps not a good idea, being logging a cross-cutting concern.
        https://en.wikipedia.org/wiki/Cross-cutting_concern"""
        ...

    @property
    @abstractmethod
    def work_dir(self) -> str:
        """A writable directory where to put our working files.
        This may contain sensitive data and should be kept secret,
        or be cleaned after use"""
        ...

    @property
    @abstractmethod
    def browsers(self) -> dict[str, AbstractBrowser]:
        """A dict of all the browsers by name."""
        ...

    @abstractmethod
    def work_path(self, file_name: str) -> str:
        """Prepends the work_dir to file_name."""
        ...
