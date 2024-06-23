class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxm = 0
        num = 0
        
        l = int(len(nums)/2) + 1
        counter = [0]*l
        
        for i in nums:
            counter[i%l] += 1
            new = counter[i%l]
            
            if (new > maxm):
                maxm = new
                num = i
                
        return num
            
        
            
        
        