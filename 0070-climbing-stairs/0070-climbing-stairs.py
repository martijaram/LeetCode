class Solution:
    def climbStairs(self, n: int) -> int:
        back0 = 1
        back1 = 1
        nextup = 1
        
        for i in range(2, n+1):
            nextup = back0 + back1
            back0 = back1
            back1 = nextup
            
        return nextup
            
            
        