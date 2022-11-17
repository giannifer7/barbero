from browsers.firefox import Bfirefox
import os


class Bfirefox_di_fede(Bfirefox):
    def __init__(self) -> None:
        self.firefox_data_base_dir = os.path.expanduser("~/snap/firefox/common/.mozilla/firefox")

    @property
    def name(self) -> str:
        return "firefox_di_fede"
