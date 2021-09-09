from utils import sort_by_current_rent, filter_by_lease_years
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
        help="Pass to system the desired item count. Default is 0.",
    )

    parser.add_argument(
        "--lease-year",
        default=25,
        type=int,
        help="Pass to system the desired lease year. Default is 25.",
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    sort_type, item_count, lease_year = (
        args.sorting_type,
        args.item,
        args.lease_year,
    )

    reader = csv.DictReader(open(CSV_PATH, "r"))
    csv_data = list(reader)
    sorted_rents = sort_by_current_rent(csv_data, sort_type, item_count)
    print(sorted_rents)  # Print to console
    filtered_rents, total_rent = filter_by_lease_years(csv_data, lease_year)
    print(filtered_rents)
    print(total_rent)


main()
