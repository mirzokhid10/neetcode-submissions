class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle=[[1]]
        
        
        for i in range(numRows-1):
            prev=triangle[i]
            arr=[1]
            for k in range(len(prev)-1):
                arr.append(prev[k]+prev[k+1])
                
            arr.append(1)
            
        
            triangle.append(arr)
        
        return triangle