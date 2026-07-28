class Solution:
    def largestGoodInteger(self, num: str) -> str:
        arr=[]
        str=""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                str=num[i] + num[i+1] + num[i+2]
                arr.append(str)
        
        if len(arr)==0:
            return ""
        else:
            return max(arr)  