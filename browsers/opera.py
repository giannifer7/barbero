import os

from abstract_browser import AbstractBrowser


class Bopera(AbstractBrowser):
    @property
    def name(self) -> str:
        return "opera"

    @property
    def db_path(self) -> str:
        return os.path.expanduser("~/.config/opera/History")

    @property
    def history_query(self) -> str:
        return """
            SELECT
                id,
                datetime(last_visit_time / 1000000 +
                    (strftime('%s', '1601-01-01')),
                    'unixepoch', 'localtime') AS date,
                url,
                title,
                visit_count AS count
            FROM
                urls
            ORDER BY
                last_visit_time desc
        """
