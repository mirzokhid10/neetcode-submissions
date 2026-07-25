class Solution:
    def kthDistinct(self, nums: List[str], k: int) -> str:
        store={}
        arr=[]    
        for i in range(len(nums)):
            store[nums[i]]=store.get(nums[i],0)+1
            
        for key, value in store.items():
            if value==1:
                arr.append(key)
        
        if k>len(arr):
            return ""
        
        return arr[k-1]