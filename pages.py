#!/usr/bin/env python3

"""
Print a csv with count and page colums, sorted by decreasing count,
from the history files of some browsers for Linux.
"""

import sys
from operator import itemgetter
from typing import Counter, TextIO

from abstract_configuration import AbstractConfiguration as Konf
from history import history_all


def page_and_count(konf: Konf) -> dict[str, int]:
    """Return dict of web pages and their visit count."""

    # Counter is a subclass of dict
    result: dict[str, int] = Counter()
    for record in history_all(konf):
        # accumulate the values with the same key
        result.update({record.url: record.xcount})
    return result


def page_by_count(konf: Konf) -> list[tuple[str, int]]:
    """Return list of pairs (page, count) sorted by decreasing visit count."""

    result = list(page_and_count(konf).items())
    result.sort(key=itemgetter(1), reverse=True)
    return result


def print_page_by_count(konf: Konf, file: TextIO = sys.stdout) -> None:
    """Print a csv of (page, count) rows to the provided file,
    sorted by decreasing visit count ."""

    for page, count in page_by_count(konf):
        print(f"{count}, {page}", file=file)


def run(konf: Konf) -> None:
    """Print a csv of (page, count) rows to sys.stdout"""

    print_page_by_count(konf)


def main() -> None:
    """Print a csv of (page, count) rows to sys.stdout
    Called when the module is executed as a script."""

    # pylint: disable=import-outside-toplevel
    from configuration import Configuration
    # pylint: enable=import-outside-toplevel

    konf = Configuration()
    run(konf)


if __name__ == "__main__":
    main()
