class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        arr=[]
        for i in nums:
            if i%2==0:
                arr.append('true')
            else:
                arr.append('false')
            
        for k in range(len(arr)-1):
            if arr[k]==arr[k+1]:
                return False
        
        return True