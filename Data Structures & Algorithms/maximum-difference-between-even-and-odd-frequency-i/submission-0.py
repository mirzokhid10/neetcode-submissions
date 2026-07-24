class Solution:
    def maxDifference(self, s: str) -> int:
        store={}
        odd=[]
        even=[]
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]]=1
            else:
                store[s[i]]+=1
        
        for val in list(store.values()):
            if val%2==1:
                odd.append(val)
            else:
                even.append(val)
        
        max_diff=max(odd)-min(even)
        
        return max_diff
        