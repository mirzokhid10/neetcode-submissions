class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
    
        map_p={}
        map_w={}
        
        if len(pattern)!=len(words):
            return False
        
        for i in range(len(pattern)):
            map_p[pattern[i]]=map_p.get(pattern[i], words[i])
        
        for k in range(len(words)):
            map_w[words[k]]=map_w.get(words[k], pattern[k])
        
        
        ans = len(map_p) == len(map_w) and all(map_w.get(v) == k for k, v in map_p.items())
        
        return ans