class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            difference = target - nums[i]
    
            if difference in store:
                return [store[difference], i]
    
            store[nums[i]] = i