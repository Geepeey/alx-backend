#!/usr/bin/python3
"""
A class MRUCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class inherits from BaseCaching"""

    def __init__(self):
        """Initializes an empty cache_data dictionary"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache_data dictionary"""
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the most recently used key (MRU)
            mru_key = next(reversed(self.cache_data))
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the new key-value pair to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Returns items in cache"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order list (MRU)
        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value

        return value
