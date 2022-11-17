
from configuration import Configuration as GeneralConfiguration
from abstract_browser import AbstractBrowser

class Configuration(GeneralConfiguration):
    """
    def __init__(self, logging_level=logging.WARNING) -> None:
        self.setup_logging(logging_level)
        self._work_dir = "_work_dir"
        os.makedirs(self._work_dir, exist_ok=True)
    """

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
