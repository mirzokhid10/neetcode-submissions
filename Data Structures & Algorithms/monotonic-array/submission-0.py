class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        arr=[]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                arr.append(True)
            elif nums[i]>nums[i+1]:
                arr.append(False)
        print(arr)
        return all(arr) or not any(arr)