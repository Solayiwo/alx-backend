#!/usr/bin/env python3

import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination information
            and deletion resilience.
        """

        assert index is not None and 0 <= index < len(
            self.__indexed_dataset), "Index out of range"

        data = []
        current_index = index
        dataset_length = len(self.__indexed_dataset)

        while len(data) < page_size and current_index < dataset_length:
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
            current_index += 1

        # Determine the next index
        next_index = current_index if current_index < dataset_length else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
