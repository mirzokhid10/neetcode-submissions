class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
       
            elements_to_right = arr[i+1:]
            highest = max(elements_to_right) if elements_to_right else -1
            arr[i]=highest

        return arr