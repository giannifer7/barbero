#!/usr/bin/env python3

"""
Print a csv from the history files of some browsers for Linux
(Chromium, Falkon, Firefox and Opera)
The columns are the fields of the Website class below, namely:
a progressive index,
the browser name,
the id in the specific browser history,
the last visit date,
the url,
the title,
the visit count.
"""

import sqlite3
from datetime import datetime
from typing import Generator, Iterable, NamedTuple
from contextlib import contextmanager

from abstract_configuration import AbstractConfiguration as Konf
from abstract_browser import AbstractBrowser


class Website(NamedTuple):
    idx: int  # progressive index
    browser: str  # browser name
    bid: int  # id in the specific browser history
    date: datetime  # last visit datetime
    url: str
    title: str
    # a "count" field leaks from the implementation
    # and upsets the type linters, hence the stupid name
    xcount: int  # visit count

    def csv_row(self) -> str:
        return repr(tuple(self))[1:-1]


def process_urls(browser: AbstractBrowser, cursor: sqlite3.Cursor) -> Iterable[Website]:
    cursor.execute(browser.history_query)
    records = cursor.fetchall()
    for idx, record in enumerate(records):
        yield Website(*((idx, browser.name) + record))


@contextmanager
def history_cursor(db_path: str) -> Generator[sqlite3.Cursor, None, None]:
    """context manager for opening a browser history db."""

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    try:
        yield cursor

    finally:
        cursor.close()
        connection.close()


def process_history(konf: Konf, browser: AbstractBrowser) -> Iterable[Website]:
    import shutil

    try:
        # browsers lock the database while open, so we work on a copy
        work_db_path = konf.work_path(browser.name + ".db")
        shutil.copy2(browser.db_path, work_db_path)
        with history_cursor(work_db_path) as cursor:
            for record in process_urls(browser, cursor):
                yield record
    except FileNotFoundError as exc:
        konf.info("history for %s not found: %s", browser.name, exc)
    except sqlite3.Error as exc:
        konf.info("could not open %s history db: %s", browser.name, exc)


def history_all(konf: Konf) -> Iterable[Website]:
    for browser in konf.browsers.values():
        for record in process_history(konf, browser):
            yield record


def print_history_all_csv(konf: Konf) -> None:
    for record in history_all(konf):
        print(record.csv_row())


def main() -> None:
    from configuration import Configuration

    konf = Configuration()
    print_history_all_csv(konf)


if __name__ == "__main__":
    main()
