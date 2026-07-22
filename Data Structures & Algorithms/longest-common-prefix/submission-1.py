class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
    
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            excepted=shortest[i]
            
            for str in strs:
                if str[i]!=excepted:
                    return prefix
            prefix+=excepted
            
        return prefix