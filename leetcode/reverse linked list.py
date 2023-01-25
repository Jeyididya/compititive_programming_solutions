# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head ==None:
            return None
        nex=None
        prev=None
        curr=head

        while curr.next:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        curr.next=prev
        return curr