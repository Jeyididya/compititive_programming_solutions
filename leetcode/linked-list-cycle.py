# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        hh = head
        tail =hh.next

        while hh !=tail:
            if tail is None or tail.next is None:
                return False
            hh =hh.next
            tail=tail.next.next
        return True