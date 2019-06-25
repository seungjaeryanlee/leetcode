"""
OrderedDict solution for Algorithms #146: LRU Cache

- GET Time Complexity: O(1)
- PUT Time Complexity: O(1)

Runtime: 100 ms, faster than 96.77% of Python3 online submissions for LRU Cache.
Memory Usage: 22 MB, less than 34.50% of Python3 online submissions for LRU Cache.
"""
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        # Need to delete since OrderedDict does not update order for value updates
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # Need to delete since OrderedDict does not update order for value updates
        if key in self.cache:
            del self.cache[key]
        elif self.size == self.capacity:
            del self.cache[next(iter(self.cache.keys()))]
        else:
            self.size += 1
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
