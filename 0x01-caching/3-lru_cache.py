#!/usr/bin/python3
"""
A class LRUCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class inherits from BaseCaching"""

    def __init__(self):
        """Initializes an empty cache_data dictionary"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item to the cache_data dictionary"""
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the least recently used key (LRU)
            lru_key = self.order[0]
            del self.cache_data[lru_key]
            self.order.pop(0)
            print(f"DISCARD: {lru_key}")

        # Add the new key-value pair to the cache
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Returns value quarred from dict"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order list (LRU)
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
