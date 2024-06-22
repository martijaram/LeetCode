class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = [0]*26
        for i in magazine:
            table[ord(i) - 97] += 1
            
        for i in ransomNote:            
            value = ord(i) - 97
            table[value] -= 1
            
            if (table[value] < 0):
                return False
                
                
            
        return True
            
        