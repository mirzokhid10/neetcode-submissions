class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort=sorted(heights)
        counter=0
        for i in range(len(heights)):
            if heights[i]!=sort[i]:
                counter+=1
        
        return counter