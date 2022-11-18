#!/usr/bin/env python3

"""
Print a csv with count and page colums, sorted by decreasing count,
from the history files of some browsers for Linux.
"""

from history import history_all
from operator import itemgetter
from abstract_configuration import AbstractConfiguration as Konf
from typing import Counter


def page_and_count(konf: Konf) -> dict[str, int]:
    result: dict[str, int] = Counter()
    for record in history_all(konf):
        result.update({record.url: record.xcount})
    return result


def page_by_count(konf: Konf) -> list[tuple[str, int]]:
    result = list(page_and_count(konf).items())
    result.sort(key=itemgetter(1), reverse=True)
    return result


def run(konf: Konf) -> None:
    for page, count in page_by_count(konf):
        print(f"{count}, {page}")


def main() -> None:
    from configuration import Configuration

    konf = Configuration()
    run(konf)


if __name__ == "__main__":
    main()
