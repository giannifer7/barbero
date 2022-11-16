from abstract_browser import AbstractBrowser
import os
import configparser


class Bfirefox(AbstractBrowser):
    def __init__(self) -> None:
        self.firefox_data_base_dir = os.path.expanduser("~/.mozilla/firefox")

    @property
    def name(self) -> str:
        return "firefox"

    def profile_path(self) -> str:
        firefox_profiles = os.path.join(self.firefox_data_base_dir, "profiles.ini")
        config = configparser.ConfigParser()
        config.read(firefox_profiles)
        profile_relative_path = ""
        for sect in config.sections():
            if sect.startswith("Profile") and config[sect]["Name"] == "default-release":
                profile_relative_path = config[sect]["Path"]
        return os.path.join(self.firefox_data_base_dir, profile_relative_path)

    @property
    def db_path(self) -> str:
        return os.path.join(self.profile_path(), "places.sqlite")

    @property
    def history_query(self) -> str:
        """see the following sites for more interesting stuff:
        https://gist.github.com/olejorgenb/9418bef65c65cd1f489557cfc08dde96
        https://forensicswiki.xyz/wiki/index.php?title=Mozilla_Firefox_3_History_File_Format
        """
        return """
            select
                moz_places.id as id,
                datetime((visit_date/1000000), 'unixepoch', 'localtime') AS visit_date,
                url,
                title,
                visit_count
            from
                moz_places
                INNER JOIN moz_historyvisits on moz_historyvisits.place_id = moz_places.id
            order by
                visit_date desc
        """
