#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """Assign the item to the cache with the specified key."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the item associated with the given key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
