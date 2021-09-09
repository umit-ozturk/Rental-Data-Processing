from utils import sort_by_current_rent
from constant import CSV_PATH
import csv


def main():
    sort_type = True  # Argparse
    n = 5  # Argparse
    reader = csv.DictReader(open(CSV_PATH, "r"))
    sorted_rents = sort_by_current_rent(list(reader), sort_type, n)
    print(sorted_rents)  # Print to console


main()
