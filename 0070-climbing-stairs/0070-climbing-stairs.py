class Solution:
    def climbStairs(self, n: int) -> int:
        back1 = 1
        nextup = 1
        
        i = 2
        while i <= n:
            nextup = back1 + nextup
            back1 = nextup - back1
            
            i += 1
            
        return nextup
            
            
        