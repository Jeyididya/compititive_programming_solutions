# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ro=[]
        curr=head
        if not head:
            return head
        nex=curr.next

        while curr.next:
            if curr.val == nex.val:
                curr.next=nex.next
                nex=nex.next
            else:
                curr=curr.next
                nex.next=nex.next
        return head