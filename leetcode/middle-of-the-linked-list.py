# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=1
        h=head
        while h.next:
            h=h.next
            count+=1
        if count%2==0:
            count=count//2+1
            h1=head
            for i in range(1,count):
                h1=h1.next
            hea=h1
        else:
            count=count//2
            h1=head
            for i in range(count):
                h1=h1.next
            hea=h1
        return hea