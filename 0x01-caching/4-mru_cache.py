#!/usr/bin/python3
"""Defines a class MRUCache that inherits from BaseCaching."""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """Least recently used (LRU) caching system."""

    def __init__(self):
        super().__init__()
        self.count = 0
        self.use_count = {}

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value of
        the key.
        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if len(self.use_count) > 0:
            mru_key = self.get_most_used()

        if key not in self.use_count:
            self.use_count.update({key: self.count})
            self.count += 1
        else:
            self.use_count.update({key: self.use_count[key] + 1})

        self.cache_data.update({key: item})

        if len(self.cache_data) > self.MAX_ITEMS:
            self.use_count.pop(mru_key)
            self.cache_data.pop(mru_key)
            print("Discard: {}".format(mru_key))

    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        if key in self.cache_data.keys():
            self.use_count[key] = self.use_count[key] + 1
            return self.cache_data.get(key)
        return None

    def get_most_used(self):
        """Returns the most used key."""
        items = [(k, v) for k, v in self.use_count.items()]
        items.sort(key=lambda item: item[1])
        duplicates = [item for item in items if item[1] == items[0][1]]
        if len(duplicates) > 1:
            return duplicates[-1][0]

        return items[-1][0]