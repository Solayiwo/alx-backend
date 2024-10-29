#!/usr/bin/env python3
"""Using index_range to find the correct indexes
    to paginate the datase
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end index for pagination."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def total_pages(self, page_size: int) -> int:
        """Calculate total number of pages available."""
        dataset_length = len(self.dataset())
        return math.ceil(dataset_length / page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of data based on page and page_size."""
        assert isinstance(page, int) and page > 0, (
            "Page must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer"
        )

        start_index, end_index = index_range(page, page_size)

        data = self.dataset()

        if page > self.total_pages(page_size):
            return []
        return data[start_index:end_index]
