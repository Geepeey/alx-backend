#!/usr/bin/python3
"""
A class LFUCache that inherits from BaseCaching and is a caching system
"""
from collections import defaultdict
from datetime import datetime
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class inherits from BaseCaching"""

    def __init__(self):
        """Initializes an empty cache_data dictionary"""
        super().__init__()
        self.key_frequency = defaultdict(int)
        self.key_last_used = {}

    def update_frequency(self, key):
        """Increase frequency of a given key"""
        self.key_frequency[key] += 1

    def update_last_used(self, key):
        """Updates the last used timestamp of a given key"""
        self.key_last_used[key] = datetime.now()

    def get_least_frequency(self):
        """Finds the keys with the least frequency"""
        min_freq = min(self.key_frequency.values())
        least_frequent_keys = [
            key for key,
            freq in self.key_frequency.items() if freq == min_freq]
        return least_frequent_keys

    def get_least_recently_used(self):
        """Finds the keys that were least recently used"""
        min_time = min(self.key_last_used.values())
        least_recently_used_keys = [
            key for key,
            time in self.key_last_used.items() if time == min_time]
        return least_recently_used_keys

    def put(self, key, item):
        """
        Puts a key-value pair in the cache while applying
        LFU and LRU eviction strategies if needed
        """
        if key is None or item is None:
            return

        # Remove the least frequency used item (LFU algorithm)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_freq_keys = self.get_least_frequency()
            if len(least_freq_keys) > 1:
                # If there are multiple keys with the same frequency,
                # remove the least recently used among them (LRU algorithm)
                least_recent_keys = self.get_least_recently_used()
                key_to_remove = min(
                    least_freq_keys, key=lambda k: self.key_last_used[k])
            else:
                key_to_remove = least_freq_keys[0]
            del self.cache_data[key_to_remove]
            del self.key_frequency[key_to_remove]
            del self.key_last_used[key_to_remove]
            print("DISCARD:", key_to_remove)

        self.cache_data[key] = item
        self.update_frequency(key)
        self.update_last_used(key)

    def get(self, key):
        """Retrieves the value from cache"""
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        self.update_last_used(key)
        return self.cache_data[key]
