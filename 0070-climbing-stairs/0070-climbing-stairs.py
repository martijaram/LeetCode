class Solution:
    def climbStairs(self, n: int) -> int:
        back0 = 1
        back1 = 1
        nextup = 1
        
        i = 2
        while i <= n:
            nextup = back1 + back0
            back0 = back1
            back1 = nextup
            
            i += 1
            
        return nextup
            
            
        