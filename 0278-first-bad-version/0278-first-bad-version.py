# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        half = int((high+low)/2)
        isit = isBadVersion(half)
 
            
        while True:
            if (isit):
                if (not isBadVersion(half-1)):
                    return half
                else:
                    high = half-1
                    half = int((low+high)/2)
            else:
                low = half + 1
            
            half = int((high+low)/2)
            
            if (half == 1):
                return half
            
            isit = isBadVersion(half)
            
    
                