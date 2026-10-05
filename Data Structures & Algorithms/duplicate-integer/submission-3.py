class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}

        for i in range(len(nums)):
            store[nums[i]] = store.get(nums[i], 0) + 1
    
        for value in store.values():
            if value > 1:
                return True
    
        return False