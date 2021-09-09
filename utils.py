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
