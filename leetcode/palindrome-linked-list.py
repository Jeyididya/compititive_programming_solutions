# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        i=head
        st=[]
        flag=True
        while i.next:
            st.append(i.val)
            i=i.next
        st.append(i.val)
        # print(st,st[::-1],st==st[::-1])
        if st==st[::-1]:
            return True
        return False