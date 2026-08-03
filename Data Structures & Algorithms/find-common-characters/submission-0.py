class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [0] * 26
        for ch in words[0]:
            common[ord(ch) - ord('a')] += 1
        
        # intersect with each next word
        for word in words[1:]:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            for i in range(26):
                common[i] = min(common[i], freq[i])
        
        # build answer
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * common[i])
        
        return result
        