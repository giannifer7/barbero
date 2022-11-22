#!/usr/bin/env python3

"""
Print a csv with count and site colums, sorted by decreasing count,
from the history files of some browsers for Linux.
"""


import sys
from operator import itemgetter
from typing import Counter, TextIO

from abstract_configuration import AbstractConfiguration as Konf
from pages import page_by_count


def site_and_count(konf: Konf) -> dict[str, int]:
    """Return dict of sites and their visit count."""

    result: dict[str, int] = Counter()
    for url, count in page_by_count(konf):
        # should we use urlparse?
        host = "/".join(url.split("/", 3)[:3])
        result.update({host: count})
    return result


def site_by_count(konf: Konf) -> list[tuple[str, int]]:
    """Return list of pairs (site, count) sorted by decreasing visit count."""

    result = list(site_and_count(konf).items())
    result.sort(key=itemgetter(1), reverse=True)
    return result


def print_site_by_count(konf: Konf, file: TextIO = sys.stdout) -> None:
    """Print a csv of (site, count) rows to the provided file,
    sorted by decreasing visit count ."""

    for site, count in site_by_count(konf):
        print(f"{count}, {site}", file=file)


def run(konf: Konf) -> None:
    """Print a csv of (site, count) rows to sys.stdout"""

    print_site_by_count(konf)


def main() -> None:
    """Print a csv of (site, count) rows to sys.stdout
    Called when the module is executed as a script."""

    # pylint: disable=import-outside-toplevel
    from configuration import Configuration
    # pylint: enable=import-outside-toplevel

    konf = Configuration()
    run(konf)


if __name__ == "__main__":
    main()
