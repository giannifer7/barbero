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

import logging
import shutil
import sqlite3
import sys
from collections.abc import Iterable, Iterator
from contextlib import contextmanager
from datetime import datetime
from typing import NamedTuple, TextIO

from abstract_browser import AbstractBrowser
from abstract_configuration import AbstractConfiguration as Konf


class Website(NamedTuple):
    """A record in the result csv."""

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
        """Strip the parentheses from the tuple representation of self."""
        return str(tuple(self))[1:-1]


def process_urls(
        browser: AbstractBrowser,
        cursor: sqlite3.Cursor
) -> Iterable[Website]:
    """Query the cursor and yield all the records."""

    cursor.execute(browser.history_query)
    for idx, record in enumerate(cursor.fetchall()):
        yield Website(*((idx, browser.name) + record))


@contextmanager
def history_cursor(db_path: str) -> Iterator[sqlite3.Cursor]:
    """Context manager for opening a browser history db."""

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    try:
        yield cursor

    finally:
        cursor.close()
        connection.close()


def process_history(konf: Konf, browser: AbstractBrowser) -> Iterable[Website]:
    """Copy the history file to the work dir,
    open the copy and yield all the records."""

    try:
        # browsers lock the database while open, so we work on a copy
        work_db_path = konf.work_path(browser.name + ".db")
        shutil.copy2(browser.db_path, work_db_path)
        with history_cursor(work_db_path) as cursor:
            yield from process_urls(browser, cursor)
    except FileNotFoundError as exc:
        konf.logger.info("history for %s not found: %s", browser.name, exc)
    except (sqlite3.Error, OSError) as exc:
        konf.logger.info("could not open %s history db: %s", browser.name, exc)


def history_all(konf: Konf) -> Iterable[Website]:
    """Yield all records from the history db of all browsers"""

    for browser in konf.browsers.values():
        yield from process_history(konf, browser)


def print_history_all_csv(konf: Konf, file: TextIO = sys.stdout) -> None:
    """Print a csv of Website rows to the provided file."""

    for record in history_all(konf):
        print(record.csv_row(), file=file)


def main() -> None:
    """Print a csv on sys.stdout with the history af all the browsers
    defined in Configuration."""

    # pylint: disable=import-outside-toplevel
    from configuration import Configuration
    # pylint: enable=import-outside-toplevel

    konf = Configuration(logging_level=logging.DEBUG)
    print_history_all_csv(konf)


if __name__ == "__main__":
    main()
