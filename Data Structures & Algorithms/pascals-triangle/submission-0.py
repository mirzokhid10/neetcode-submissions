class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
    
        triangle=[[1]]
        
        for k in range(numRows-1):
            triangle.append(generateArr(triangle[k]))
        
        return triangle


def generateArr(prev):
    
    arr=[1]
    sum=0
    for i in range(len(prev)-1):
        sum=prev[i]+prev[i+1]
        arr.append(sum)
    arr.append(1)
        
    
    return arr
prev = [1]
print(generateArr(prev))