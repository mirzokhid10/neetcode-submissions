class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_on_right = -1
    
            for k in range(i + 1, len(arr)):
                max_on_right = max(max_on_right, arr[k])
            arr[i] = max_on_right

        return arr