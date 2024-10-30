#!/usr/bin/env python3
""" LRUCache module """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU Caching system that inherit from BaseCaching"""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.cache_order = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with LRU eviction if necessary."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.pop(key)
            self.cache_data[key] = item
            self.cache_order[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_order.popitem(last=False)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve an item from the cache by key and mark
            it as recently used.
        """
        if key in self.cache_data:
            self.cache_order.move_to_end(key)
            return self.cache_data[key]
        return None
