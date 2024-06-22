class Solution:
    def longestPalindrome(self, s: str) -> int:
        l = 0
        m = 0
        
        hashtable = [0]*58
        
        for i in s:
            hashtable[ord(i)-65] += 1
            
        for i in hashtable:
            if (i % 2 == 0):
                l += i
            else:
                l += i-1
                
                if (m == 0):
                    m = 1
                
        return l + m
            