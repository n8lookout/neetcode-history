# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        previous, current = head, head.next
        toInsert = False

        while True:
            if previous.val <= insertVal <= current.val:
                toInsert = True
            elif previous.val > current.val:
                if insertVal >= previous.val or insertVal <= current.val:
                    toInsert = True

            if toInsert:
                previous.next = Node(insertVal, current)
                return head
            
            previous, current = current, current.next
            if previous == head:
                break
        
        previous.next = Node(insertVal, current)           
        return head