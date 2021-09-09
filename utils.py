def sort_by_current_rent(data, sort_type=False, n=5):
    """
    Sorts the data by current rent.
    :param data: Data which is coming from reader.
    :param sort_type: Boolean, Sorting Type.
    :param n: Int, Item count.
    :return: Sorted data which is contain current rents.
    """
    return sorted(
        data, key=lambda x: float(x["Current Rent"]), reverse=sort_type
    )[:n]
