class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        triangle=[[1]]
        
        
        for i in range(rowIndex):
            prev=triangle[i]
            arr=[1]
            for k in range(len(prev)-1):
                arr.append(prev[k]+prev[k+1])
                
            arr.append(1)
            
        
            triangle.append(arr)
        
        return triangle[rowIndex]
        