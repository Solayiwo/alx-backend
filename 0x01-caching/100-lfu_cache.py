#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """LFU Caching system that inherit from BaseCaching"""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with LFU eviction if necessary."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [
                        k for k in self.usage_order
                        if self.frequency[k] == min_freq
                    ]
                lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.usage_order.pop(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key and update
            its usage frequency.
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
            return self.cache_data[key]
        return None
