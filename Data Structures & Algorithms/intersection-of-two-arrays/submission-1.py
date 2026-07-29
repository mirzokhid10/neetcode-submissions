class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store=set(nums1)
        result=set()
        
        for i in range(len(nums2)):
            if nums2[i] in store:
                result.add(nums2[i])
            
        return list(result)