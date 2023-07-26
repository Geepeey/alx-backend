#!/usr/bin/python3
"""
A class FIFOCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class inherits from BaseCaching"""

    def __init__(self):
        """Initializes an empty cache_data dictionary"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache_data dictionary"""
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the first item put in cache (FIFO)
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        # Add the new key-value pair to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves value/item"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
