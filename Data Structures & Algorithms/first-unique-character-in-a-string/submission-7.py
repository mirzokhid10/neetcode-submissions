class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            
        for key in list(freq):
            if freq[key] > 1:
                del freq[key] 
        
        if len(freq)==0:
            return -1
        else:
            return s.index(next(iter(freq)))