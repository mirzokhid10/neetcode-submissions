class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran={}
        mag={}
        
        for k in ransomNote:
            ran[k]=ran.get(k,0)+1
        for j in magazine:
                mag[j]=mag.get(j,0)+1
    
        is_inside = all(mag.get(k, 0) >= v for k, v in ran.items())
            
        return is_inside