"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        current = head
        while current:
            oldToCopy[current].val = current.val
            oldToCopy[current].next = oldToCopy[current.next]
            oldToCopy[current].random = oldToCopy[current.random]
            current = current.next
        return oldToCopy[head]