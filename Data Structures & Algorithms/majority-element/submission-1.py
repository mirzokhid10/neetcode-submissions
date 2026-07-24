class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store={}
        candidate=None
        for i in range(len(nums)):
            candidate=nums[i]
            if candidate not in store:
                store[candidate]=1
            else:
                store[candidate]+=1
        
        keys = list(store.keys())
        arrs = list(store.values())
        
        lar = arrs[0]
        best_index = 0 
        
        for i in range(len(arrs)):
            if arrs[i] > lar:
                lar = arrs[i]
                best_index = i
                
        if lar > len(nums) // 2:
            return keys[best_index]