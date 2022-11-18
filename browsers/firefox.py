from abstract_browser import AbstractBrowser
import os
import configparser


class Bfirefox(AbstractBrowser):
    def __init__(self) -> None:
        self.firefox_data_base_dir = os.path.expanduser("~/.mozilla/firefox")

    @property
    def name(self) -> str:
        return "firefox"

    def db_dir(self) -> str:
        config = configparser.ConfigParser()
        config.read(os.path.join(self.firefox_data_base_dir, "profiles.ini"))
        db_relative_dir = ""
        for sect in config.sections():
            if sect.startswith("Profile") and config[sect]["Name"] == "default-release":
                db_relative_dir = config[sect]["Path"]
                break
        return os.path.join(self.firefox_data_base_dir, db_relative_dir)

    @property
    def db_path(self) -> str:
        return os.path.join(self.db_dir(), "places.sqlite")

    @property
    def history_query(self) -> str:
        """https://gist.github.com/olejorgenb/9418bef65c65cd1f489557cfc08dde96
        https://forensicswiki.xyz/wiki/index.php?title=Mozilla_Firefox_3_History_File_Format
        """
        return """
            SELECT
                moz_places.id as id,
                datetime((visit_date/1000000), 'unixepoch', 'localtime') AS date,
                url,
                title,
                visit_count AS count
            FROM
                moz_places
                INNER JOIN moz_historyvisits ON moz_historyvisits.place_id = moz_places.id
            ORDER BY
                visit_date desc
        """
