#!/usr/bin/python3
"""
 A class BasicCache that inherits from BaseCaching
 and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching"""

    def put(self, key, item):
        """Assigning Arg"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve value of Arg"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
