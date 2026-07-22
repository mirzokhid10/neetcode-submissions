class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current=0
        max_count=0
        
        for i in range(len(nums)):
            if nums[i]==1:
                current+=nums[i]
            else:          
                current=0
    
            max_count = max(max_count, current)
            
                
        return max_count