class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store={}
        for i in range(len(nums)):
            store[nums[i]]=store.get(nums[i],0)+1
        
        arr=list(store.values())
        for k in range(len(arr)):
            if arr[k]%2==1:
                return False
                break
        
        return True