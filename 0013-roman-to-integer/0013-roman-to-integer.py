class Solution:
    def romanToInt(self, s: str) -> int:
        track = 0
        last = "N"
        
        lib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for i in s:
            if i is 'V' and last is 'I':
                track += 3
                print("WORKS -> " + last + i)
            elif i == 'X' and last == 'I':
                track += 8
                print("WORKS -> " + last + i)

            elif i == 'L' and last == 'X':
                track += 30
                print("WORKS -> " + last + i)

            elif i == 'C' and last == 'X':
                track += 80
                print("WORKS -> " + last + i)
            elif i == 'D' and last == 'C':
                track += 300
                print("WORKS -> " + last + i)
            elif i == 'M' and last == 'C':
                track += 800
                print("WORKS -> " + last + i)
            else:
                track += lib[i]
                print("debug -> " + last + i)
            
            last = i
            
        
        print("_________________")
        return track
        