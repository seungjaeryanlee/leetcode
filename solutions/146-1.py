"""
Solution for Algorithms #146: LRU Cache

- N: Number of operations
- C: Capacity
- Space Complexity: O(C)
- Time Complexity: O(NC)
  - Updating key_queue currently uses .remove(), which is O(C).

Runtime: 532 ms, faster than 7.34% of Python3 online submissions for LRU Cache.
Memory Usage: 21.6 MB, less than 87.29% of Python3 online submissions for LRU Cache.
"""
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Dictionary mapping keys to values
        self.cache = {}
        # Queue of keys to implement Least Recently Used (LRU)
        self.key_queue = deque([], maxlen=self.capacity)

    def _update_key_queue(self, key):
        """Send 'existing' key in key_queue the end."""
        # TODO This update is O(capacity), not O(1)
        self.key_queue.remove(key)
        self.key_queue.append(key)

    def get(self, key: int) -> int:
        if key in self.cache:
            self._update_key_queue(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Insert key-value pair if needed
        if key not in self.cache:
            if len(self.key_queue) >= self.capacity:
                del self.cache[self.key_queue[0]]
            self.key_queue.append(key)
        else:
            self._update_key_queue(key)

        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
