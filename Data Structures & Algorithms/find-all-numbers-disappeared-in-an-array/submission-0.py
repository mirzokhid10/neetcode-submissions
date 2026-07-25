class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(1, len(nums)+1):
            if i not in nums:
                arr.append(i)
        return arr