class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la = len(a)
        lb = len(b)
        fix = abs(la-lb)
        
        if (la > lb):
            b = '0'*fix + b
            lb += fix
        else:
            a = '0'*fix + a
            la += fix
            
        
        final = ''
        result = 0
        carry = 0
        
        print('a: ' + a)
        print('b: ' + b)
        
        i = 0
        while i < la:
            result = (int(a[-i - 1]) + int(b[-i - 1]) + carry)
            final = str(result%2) + final
            carry = int(result > 1)
            
            print(result)
            print(final)
            print(carry)
            print("---")
            
            
            i += 1
            
        
        if (carry == 1):
            final = str(carry) + final

        return final
            
        
        
        