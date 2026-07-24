class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        global_max = 1
        
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                inc+=1       # increment inc
                dec=1       # reset dec
            elif nums[i]<nums[i-1]:
                dec+=1       # increment dec
                inc=1       # reset inc
            else:
                inc=1       # reset both
                dec=1
            
            global_max = max(global_max, inc, dec)  # update max
        
        return global_max