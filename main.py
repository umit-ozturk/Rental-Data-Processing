from utils import (
    sort_by_current_rent,
    filter_by_lease_years,
    get_tenant_names_and_counts,
    list_rentals_by_date_range,
)
from constant import CSV_PATH
from datetime import datetime
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

    parser.add_argument(
        "--start-date",
        default=datetime.strptime("01 Jun 1999", "%d %b %Y"),
        type=lambda d: datetime.strptime(d, "%d %b %Y"),
        help="Default is ascending. If you want to sort "
        "descending send the parameter as True",
    )

    parser.add_argument(
        "--end-date",
        default=datetime.strptime("31 Aug 2007", "%d %b %Y"),
        type=lambda d: datetime.strptime(d, "%d %b %Y"),
        help="Default is ascending. If you want to sort "
        "descending send the parameter as True",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    sort_type, item_count, lease_year, start_date, end_date = (
        args.sorting_type,
        args.item,
        args.lease_year,
        args.start_date,
        args.end_date,
    )

    reader = csv.DictReader(open(CSV_PATH, "r"))
    csv_data = list(reader)
    sorted_rents = sort_by_current_rent(csv_data, sort_type, item_count)
    print(sorted_rents)  # Print to console
    print("+" * 50)
    filtered_rents, total_rent = filter_by_lease_years(csv_data, lease_year)
    print(filtered_rents, total_rent)
    print("-" * 50)
    tenant_summary_data = get_tenant_names_and_counts(csv_data)
    print(tenant_summary_data)
    print("*" * 50)
    filtered_rents_by_date_range = list_rentals_by_date_range(
        csv_data, start_date, end_date
    )
    print(
        {
            "start_date": datetime.strftime(start_date, "%d/%m/%y"),
            "end_date": datetime.strftime(end_date, "%d/%m/%y"),
            "data": filtered_rents_by_date_range,
        }
    )


main()
