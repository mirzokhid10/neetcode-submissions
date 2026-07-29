class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        tot=0
        has_odd = False
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        
        for val in freq.values():
            if val%2==0:
                tot+=val
            else:
                tot += val - 1 
                has_odd = True 
        if has_odd:
            tot += 1   
    
        return tot