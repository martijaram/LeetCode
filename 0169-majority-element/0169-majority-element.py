class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxm = 0
        num = 0
        
        counter = [0]*11
        
        for i in nums:
            index = i%10
            if counter[index] == 0:
                counter[index] = [[i, 1]]
                
                if (maxm < 1):
                    maxm = 1
                    num = counter[index][0][0]
            else:
                found = False
                for info in counter[index]:
                    if (info[0] == i):
                        info[1] += 1
                        possiblemax = info[1]
                        if (possiblemax > maxm):
                            maxm = possiblemax
                            num = info[0]
                            
                        break
                    
                    counter[index].append([i, 1])
                
        return num
            
        
            
        
        