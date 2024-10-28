#!/usr/bin/env python3

import csv
import math
from typing import Tuple, List, Dict



def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indexes for a given page and page size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the dataset page for the given pagination parameters."""
        assert isinstance(page, int) and page > 0, (
            "Page must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page size must be a positive integer"
        )

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination details."""
        data = self.get_page(page, page_size)
        total_records = len(self.dataset())
        total_pages = math.ceil(total_records / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
