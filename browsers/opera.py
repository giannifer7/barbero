from abstract_browser import AbstractBrowser
import os


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
            select
                id,
                datetime(last_visit_time / 1000000 +
                    (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'),
                url,
                title,
                visit_count
            from
                urls
            order by
                last_visit_time desc
        """
