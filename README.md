# Rental Data Processing - Test

## Installation
Clone the repository and create a virtual environment.

    $ git clone https://github.com/umit-ozturk/Rental-Data-Processing.git
	$ cd Rental-Data-Processing
	$ virtualenv -p python3 env
	$ source env/bin/activate
    $ pip install -r requirements.txt

## Running

Basically to see all data,

    $ python main.py

There are some parameters in the script. These are sorting type, item, lease year, start date and end date. The script consists of 4 parts. sorting by current rent, filter by lease year, tenant names and their counts and rental data by a date range.

1- Sorting by current rent

    $ python main.py --sorting-type True --item 5

Sorting type is False as default. False is sorting ascending and True is sorting descending.
Item determines the number of returned items

2- Filter by lease year

    $ python main.py --lease-year 25

3- List rentals by date range

    $ python main.py --start-date "01 Jun 1999" --end-date "31 Aug 2007"

To use a date range for filtering give the date as a string.

## Test

    $ pytest

## Coverage Tests

    $ coverage run -m pytest tests
    $ coverage report
