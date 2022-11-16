from abstract_browser import AbstractBrowser
import os


class Bfalkon(AbstractBrowser):
    @property
    def name(self) -> str:
        return "falkon"

    @property
    def db_path(self) -> str:
        return os.path.expanduser("~/.config/falkon/profiles/default/browsedata.db")

    @property
    def history_query(self) -> str:
        return """
            select
                id,
                datetime(date / 1000 +
                    (strftime('%s', '1970-01-01')), 'unixepoch', 'localtime'),
                url,
                title,
                count
            from
                history
            order by
                date desc
        """