# barbero

gather history files from browsers


* GitHub: <https://github.com/giannifer7/barbero>
* Free software: MIT


## Features

Generate csv files from the history files of the browsers:

    * Chromium
    * Falkon
    * Firefox
    * Opera

On Linux only, for now, but porting to other platforms and browsers
should be straightforward.

Does not depend on any external package, no need to install:
just clone and hack.

There are 3 executable scripts that write a csv to the standard output:

    * history.py
    * pages.py
    * sites.py


### history.py

Print some fields common to all browsers' histories

Usage: ./history.py > history.csv

The csv fields are:

    * idx: int  # progressive index
    * browser: str  # browser name
    * bid: int # id in the specific browser history
    * date: datetime # last visit datetime
    * url: str
    * title: str
    * xcount: int # visit count


### pages.py

Visited pages in decreasing order of visit counts.

Usage: ./pages.py > pages.csv

The csv fields are:

    * the visit count
    * the url


### sites.py

Visited sites in decreasing order of visit counts.

Usage: ./sites.py > sites.csv

The csv fields are:

    * the visit count
    * the url


* TODO
    * tests
    * documentation
    * make it more pythonic
    * more platforms
    * more browsers


If you have any complaint about this less-than-alpha quality software, then "VENITE A BRUCIARMI LA CASA!"

* The project is named after the famous italian historian Alessandro Barbero
    https://it.wikipedia.org/wiki/Alessandro_Barbero

