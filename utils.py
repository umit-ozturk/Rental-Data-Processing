from datetimerange import DateTimeRange
import itertools
import operator


def sort_by_current_rent(data, sort_type=False, n=5):
    """
    Sorts data by current rent.
    :param data: Data which is coming from reader.
    :param sort_type: Boolean, Sorting Type.
    :param n: Int, Item count.
    :return: Sorted data which is contain current rents.
    """
    return sorted(
        data, key=lambda x: float(x["Current Rent"]), reverse=sort_type
    )[:n]


def filter_by_lease_years(data, year=25):
    """
    Filters data by lease date.
    :param data: Data which is coming from reader.
    :param year: Int, Lease Years
    :return: Filtered data, Total Rent
    """
    filtered_data = list(filter(lambda x: x["Lease Years"] == str(year), data))
    total = sum([float(value["Current Rent"]) for value in filtered_data])
    return filtered_data, total


def get_tenant_names_and_counts(data):
    """
    Return tenant names and record counts
    :param data: Data which is coming from reader.
    :return: List of tenant records and their counts
    """
    o = {}
    for i, g in itertools.groupby(
        data, key=operator.itemgetter("Tenant Name")
    ):
        if i in o.keys():  # Exist check
            o[i] += 1
        else:
            o[i] = len(list(g))
    return [{"Tenant Name": k, "Count": v} for k, v in o.items()]


def check_datetime_in_range(start, end, date):
    """
    Returns related date is in the range or not.
    :param start: Datetime object, Start Date
    :param end: Datetime object, End Date
    :param date: Datetime object, Date which is queried
    :return: Boolean
    """
    return date in DateTimeRange(start, end)


def list_rentals_by_date_range(data, start_date, end_date):
    """
    Lists data for rentals by a date range.
    :param data: Data which is coming from reader.
    :param start_date: Datetime object, Start Date
    :param end_date: Datetime object, End Date
    :return: List of rental record between desired dates, Start date and
    end date.
    """
    filtered_data = list(
        filter(
            lambda x: check_datetime_in_range(
                start_date, end_date, x["Lease Start Date"]
            ),
            data,
        )
    )
    return filtered_data
