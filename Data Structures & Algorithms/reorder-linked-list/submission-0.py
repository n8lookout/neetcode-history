# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverseList = slow.next
        prev = slow.next = None
        while reverseList:
            temp = reverseList.next
            reverseList.next = prev
            prev = reverseList
            reverseList = temp

        firstHead, reverseList = head, prev
        while reverseList:
            tmp1, tmp2 = firstHead.next, reverseList.next
            firstHead.next = reverseList
            reverseList.next = tmp1
            firstHead, reverseList = tmp1, tmp2
