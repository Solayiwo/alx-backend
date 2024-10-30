#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching system that inherit from BaseCaching"""
    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.last_key = None  # Track the last key added

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction if necessary."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key in self.cache_data:
                    print(f"DISCARD: {self.last_key}")
                    del self.cache_data[self.last_key]
            self.last_key = key

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key, None)
