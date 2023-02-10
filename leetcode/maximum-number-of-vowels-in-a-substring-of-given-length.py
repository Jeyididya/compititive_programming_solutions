class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        count=0
        ma=0
        le=len(s)
        for j in range(le):
            if s[j] in 'aeiou':
                count+=1
            if j-i+1==k:
                ma=max(ma,count)
                if s[i] in 'aeiou':
                    count-=1
                i+=1
        return ma