#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end index for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end
        index for the items on the page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
