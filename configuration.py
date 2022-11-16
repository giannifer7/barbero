"""
Configuration and logging, created in the main
and passed to all the top level functions.
"""


import os
import logging

from abstract_configuration import AbstractConfiguration
from abstract_browser import AbstractBrowser


class Configuration(AbstractConfiguration):
    def __init__(self, logging_level=logging.WARNING) -> None:
        self.setup_logging(logging_level)
        self._work_dir = "_work_dir"
        os.makedirs(self._work_dir, exist_ok=True)

    def setup_logging(self, logging_level, logger_name="base") -> None:
        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler("history.log")
        file_handler.setLevel(logging.DEBUG)
        # file_handler.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging_level)
        # create formatter and add it to the handlers
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        # add the handlers to _logger
        self._logger.addHandler(console_handler)
        self._logger.addHandler(file_handler)

    def debug(self, *args, **kwargs) -> None:
        self._logger.debug(*args, **kwargs)

    def info(self, *args, **kwargs) -> None:
        self._logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs) -> None:
        self._logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs) -> None:
        self._logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs) -> None:
        self._logger.critical(*args, **kwargs)

    def work_path(self, f) -> str:
        return os.path.join(self._work_dir, f)

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @property
    def work_dir(self) -> str:
        return self._work_dir

    @property
    def browsers(self) -> dict[str, AbstractBrowser]:
        from browsers.chromium import Bchromium
        from browsers.falkon import Bfalkon
        from browsers.firefox import Bfirefox
        from browsers.opera import Bopera

        return dict(
            chromium=Bchromium(),
            firefox=Bfirefox(),
            falkon=Bfalkon(),
            opera=Bopera(),
        )
