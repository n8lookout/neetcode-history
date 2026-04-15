class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0

        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1 # Out of bounds or empty list

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next: # list empty prior to insertion
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index and current:
            i += 1
            current = current.next

        # Remove the node ahead of current
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.head.next
        result = []

        while current:
            result.append(current.val)
            current = current.next
        return result
