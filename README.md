correl-o-mat
=========
correl-o-mat is a python script for analyzing correlations from the data of the wahl-o-mat (http://www.bpb.de/politik/wahlen/wahl-o-mat/).

It generates a table with all the answers of all parties for every question in the wahl-o-mat.
In addition, it generates a correlation matrix counting all questions where the
parties agree with each other. This shows, which parties share their opinions and
therefor are similar to each other. Thereby the correlation matrix also suggests which parties could
form coalitions and which parties better do not because they are too different from
each other.

System Requirements
-------------------
Tested on Mac OS X 10.8.4 with Python 2.7.3.. However the script should also run on Linux or Windows.

Usage
-----

1. Download the `wahlomat.zip` file for an election, e.g. for [Bayern 2013](http://www.bpb.de/politik/wahlen/wahl-o-mat/166512/download)
or from the [wahl-o-mat archive](http://www.bpb.de/politik/wahlen/wahl-o-mat/45817/weitere-wahlen) .

2. Run the correlomat script giving the path to `wahlomat.zip` file as the only argument
```
python correlomat.py wahlomat.zip
```
This will generate two files in the working directory of the script. The file `table.csv` holds the
answers of all parties to all questions. The file `correlation.csv` contains the correlation matrix
of all parties, showing the number of the questions each party agrees on with the other parties.


Enjoy!


