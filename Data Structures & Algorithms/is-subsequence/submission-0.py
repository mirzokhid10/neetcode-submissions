class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        str=len(s)
        torg=len(t)
        
        if s=="": return True
        if str>torg: return False
        
        j=0
        for i in range(torg):
            if t[i]==s[j]:
                if j==str-1:
                    return True
                j+=1
            
        return False