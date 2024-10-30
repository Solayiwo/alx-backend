#!/usr/bin/env python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching system that inherit from BaseCaching"""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction if necessary."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_order.remove(key)
            self.cache_data[key] = item
            self.cache_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.cache_order.pop(0)
                print(f"DISCARD: {oldest_key}")
                del self.cache_data[oldest_key]

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key, None)
