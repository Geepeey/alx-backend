#!/usr/bin/python3
"""
A class LIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class inherits from BaseCaching"""

    def __init__(self):
        """Initializes an empty cache_data dictionary"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache_data dictionary"""
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last item put in cache (LIFO)
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        # Add the new key-value pair to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Return value in cache dict"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
