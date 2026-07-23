class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        w=""
        res=[]
        for i in range(len(words)):
            w=words[i]
            
            for word in words:
                if w in word and w != word:
                    res.append(w)
                    break
            
        return res