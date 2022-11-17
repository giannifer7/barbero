import logging

from configuration import Configuration as GeneralConfiguration
from abstract_browser import AbstractBrowser


class Configuration(GeneralConfiguration):
    def __init__(self):
        super().__init__(logging_level=logging.DEBUG)

    @property
    def browsers(self) -> dict[str, AbstractBrowser]:
        from browsers.chromium import Bchromium
        from browsers.falkon import Bfalkon
        from browsers.firefox import Bfirefox
        from browsers.opera import Bopera
        from browsers.firefox_di_fede import Bfirefox_di_fede

        return dict(
            chromium=Bchromium(),
            firefox=Bfirefox(),
            falkon=Bfalkon(),
            opera=Bopera(),
            firefox_di_fede=Bfirefox_di_fede(),
        )
