class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m_n=None
        seen = set()
        duplicates = []
        for i in range(len(nums)):
            if nums[i] in seen:
                duplicates.append(nums[i])
            else:
                seen.add(nums[i])
            if i+1 not in nums:
                m_n=i+1
                
            
        
        return [duplicates[0],m_n]