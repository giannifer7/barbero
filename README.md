# barbero

Gather history files from browsers.


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

Does not depend on any external package, no installation needed,
just clone and hack:


```bash
git clone https://github.com/giannifer7/barbero.git
cd barbero
./history.py > history.csv
```


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


### TODO
    * tests
    * documentation
    * more platforms
    * more browsers


### WARNING: the history databases are copied into the work_dir directory, keep it private or clean it after use.

The project is named after the famous italian historian Alessandro Barbero.
