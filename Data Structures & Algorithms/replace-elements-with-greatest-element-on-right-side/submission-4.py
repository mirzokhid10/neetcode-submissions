class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        list=[]
        for i in range(len(arr)):
            
            elements_to_right = arr[i+1:]
            if elements_to_right:
                highest = max(elements_to_right)
            else:
                highest = -1
            
            list.append(highest)
        return list