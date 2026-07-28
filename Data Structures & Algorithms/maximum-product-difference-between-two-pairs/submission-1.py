class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        small=nums[0]*nums[1]
        large=nums[n-1]*nums[n-2]
        return large-small