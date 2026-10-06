class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            store[nums[i]] = store.get(nums[i], 0) + 1
    
        arr = sorted(store, key=store.get, reverse=True)
    
        return arr[:k]