class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table0 = [0]*26
        for i in ransomNote:
            table0[ord(i) - 97] += 1
            
        table1 = [0]*26
        for i in magazine:
            table1[ord(i) - 97] += 1
            
            decision = 0
            n = 0
            for i in table1:
                if i >= table0[n]:
                    decision += 1
                n += 1
            
            if decision >= 26:
                return True
                
                
            
        return False
            
        