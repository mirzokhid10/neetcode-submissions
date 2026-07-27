class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        letters=['b', 'a', 'l', 'o', 'n']
        for i in text:
            if i in letters:
                freq[i]=freq.get(i, 0) + 1
        
        capacity = {}
        for key in letters:
            val=freq.get(key, 0)
            if key == 'l' or key == 'o':
                capacity[key] = val // 2
            else:
                capacity[key] = val // 1
        
        ans=min(capacity.values()) 
        return ans