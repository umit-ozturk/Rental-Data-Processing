def sort_by_current_rent(data, sort_type=False, n=5):
    """

    :param data:
    :param sort_type: Boolean (asc --> False, desc --> True)
    :param n:
    :return:
    """
    return sorted(
        data, key=lambda x: float(x["Current Rent"]), reverse=sort_type
    )[:n]
