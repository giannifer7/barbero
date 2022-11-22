"""
Configuration and logging, created in the main
and passed to all the top level functions.
"""


import logging
import os
from importlib import import_module

from abstract_browser import AbstractBrowser
from abstract_configuration import AbstractConfiguration


class Configuration(AbstractConfiguration):
    """Configuration and logging class, intended to be created by the caller
    of the library and passed to the library functions.
    This helps avoiding globals,
    see https://en.wikipedia.org/wiki/Dependency_injection"""

    def __init__(self, logging_level: int = logging.WARNING) -> None:
        """Setup the logger, define and create the work_dir."""

        self.setup_logging(logging_level)
        self._work_dir = "_work_dir"
        os.makedirs(self._work_dir, exist_ok=True)
        self.setup_browsers()

    def setup_browsers(self) -> None:
        """Dynamically load the browser classes from the browsers package."""

        self._browsers: dict[str, AbstractBrowser] = {}
        script_dir = os.path.dirname(__file__)
        browser_modules_dir = "browsers"
        for file_name in os.listdir(os.path.join(
                    script_dir,
                    browser_modules_dir
                    )):
            base, ext = os.path.splitext(file_name)
            if ext != ".py" or base == "__init__":
                continue
            try:
                browser_module = import_module(
                    f"{browser_modules_dir}.{base}", browser_modules_dir
                )
                browser_class = getattr(browser_module, "B" + base)
                self._browsers[base] = browser_class()
            except (FileNotFoundError, OSError, AttributeError, RuntimeError):
                self.logger.exception("Loading %s browser class failed.", base)

    def setup_logging(self, logging_level: int,
                      logger_name: str = "history") -> None:
        """Configure a logger to be exposed in the logger property."""

        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler("history.log")
        file_handler.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(console_handler)
        self._logger.addHandler(file_handler)

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @property
    def work_dir(self) -> str:
        return self._work_dir

    def work_path(self, file_name: str) -> str:
        return os.path.join(self._work_dir, file_name)

    @property
    def browsers(self) -> dict[str, AbstractBrowser]:
        return self._browsers
