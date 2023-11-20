class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        # j=0
        ans = ""
        while i < len(word1) and i < len(word2):
            print(i)
            ans += word1[i]
            ans += word2[i]
            i += 1
        if i >= len(word1):
            ans += word2[i:]
        elif i >= len(word2):
            ans += word1[i:]
        return ans
