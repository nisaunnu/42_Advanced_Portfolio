def count_in_list(lst: list, element: any) -> int:
    """Counts the number of occurrences of an element in a list.

    Args:
        lst (list): the list to search into.
        element (any): the element to count.

    Returns:
        int: the number of times element appears in lst.
    """

    return lst.count(element)
