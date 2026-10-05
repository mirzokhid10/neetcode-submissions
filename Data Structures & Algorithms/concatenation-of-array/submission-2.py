class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        l = len(nums)
    
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + l] = nums[i]
    
        return ans