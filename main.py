from utils import sort_by_current_rent
from constant import CSV_PATH
import argparse
import csv


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Process and output the data created for tenants."
    )
    parser.add_argument(
        "--sorting-type",
        default=False,
        type=lambda x: (str(x).lower() == "true"),
        help="Default is ascending. If you want to sort "
        "descending send the parameter as True",
    )
    parser.add_argument(
        "--item",
        default=5,
        type=int,
        help="Returning item count. Default is 0. ",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    sort_type, item_count = args.sorting_type, args.item

    reader = csv.DictReader(open(CSV_PATH, "r"))
    sorted_rents = sort_by_current_rent(list(reader), sort_type, item_count)
    print(sorted_rents)  # Print to console


main()
