class Solution:
    def climbStairs(self, n: int) -> int:
        back0 = 1
        back1 = 1
        nextup = 1
        
        while n != 1:
            nextup = back1 + back0
            back0 = back1
            back1 = nextup
            
            n -= 1
            
        return nextup
            
            
        