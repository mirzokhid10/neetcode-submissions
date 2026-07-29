class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        freq={}
        max_len = -1
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=i
            else:
                current_distance = i - freq[s[i]] - 1
                max_len=max(max_len, current_distance)
                
            
        return max_len