"""
DoubleLinkedList + Dict Solution for Algorithms #146: LRU Cache

- GET Time Complexity: O(1)
- PUT Time Complexity: O(1)

Runtime: 148 ms, faster than 36.82% of Python3 online submissions for LRU Cache.
Memory Usage: 22 MB, less than 33.26% of Python3 online submissions for LRU Cache.
"""
class DoubleLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev_node = None
        self.next_node = None


class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleLinkedListNode(None, None)
        self.tail = DoubleLinkedListNode(None, None)
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.size = 0

    def add(self, node: DoubleLinkedListNode):
        """
        Add node on the left.
        """
        node_after = self.head.next_node
        self.head.next_node = node
        node_after.prev_node = node
        node.prev_node = self.head
        node.next_node = node_after

        self.size += 1

    def remove(self, node: DoubleLinkedListNode):
        """
        Remove given node.
        """
        node_before = node.prev_node
        node_after = node.next_node
        node_before.next_node = node_after
        node_after.prev_node = node_before

        self.size -= 1

    def move_to_front(self, node: DoubleLinkedListNode):
        self.remove(node)
        self.add(node)

    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append('({}, {})'.format(current.key, current.val))
            current = current.next_node

        return 'Size: {} | '.format(self.size) + ' '.join(nodes)

class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node_dict = {}
        self.key_list = DoubleLinkedList()

        self.capacity = capacity

    def get(self, key: int) -> int:
        # Edge case
        if not self.capacity: return -1

        # print('GET {}: '.format(key))
        # print('List: ', self.key_list)
        # print('Dict: ', list(self.key_to_node_dict.keys()))

        if key in self.key_to_node_dict:
            self.key_list.move_to_front(self.key_to_node_dict[key])
            # print('List: ', self.key_list)
            # print('Dict: ', list(self.key_to_node_dict.keys()))
            return self.key_to_node_dict[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        # Edge case
        if not self.capacity: return

        # print('PUT {}->{}: '.format(key, value))
        # print('List: ', self.key_list)
        # print('Dict: ', list(self.key_to_node_dict.keys()))

        if key in self.key_to_node_dict:
            self.key_list.move_to_front(self.key_to_node_dict[key])
            self.key_to_node_dict[key].val = value
        else:
            if self.key_list.size == self.capacity:
                del self.key_to_node_dict[self.key_list.tail.prev_node.key]
                if self.key_list.size:
                    self.key_list.remove(self.key_list.tail.prev_node)
            self.key_to_node_dict[key] = DoubleLinkedListNode(key, value)
            self.key_list.add(self.key_to_node_dict[key])

        # print('List: ', self.key_list)
        # print('Dict: ', list(self.key_to_node_dict.keys()))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
