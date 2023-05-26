class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s=s.lower()
        s= re.sub(r'\W+|_', '',s)
        if s==s[::-1]:
            return True
        return False
