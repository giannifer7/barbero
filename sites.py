#!/usr/bin/env python

"""
Print a csv with count and site colums, sorted by decreasing count,
from the history files of some browsers for Linux.
"""


from pages import page_by_count
from operator import itemgetter
from abstract_configuration import AbstractConfiguration as Konf
from typing import Counter


def site_and_count(konf: Konf) -> dict[str, int]:
    result: dict[str, int] = Counter()
    for url, count in page_by_count(konf):
        # should we use urlparse?
        host = "/".join(url.split("/", 3)[:3])
        result.update({host: count})
    return result


def site_by_count(konf: Konf) -> list[tuple[str, int]]:
    result = list(site_and_count(konf).items())
    result.sort(key=itemgetter(1), reverse=True)
    return result


def run(konf: Konf) -> None:
    for site, count in site_by_count(konf):
        print(f"{count}, {site}")


def main() -> None:
    from configuration import Configuration

    konf = Configuration()
    run(konf)


if __name__ == "__main__":
    main()
