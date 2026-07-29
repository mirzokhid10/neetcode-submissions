class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        store={}
        n=len(words)
        for i in range(len(words)):
            for k in range(len(words[i])):
                store[words[i][k]]=store.get(words[i][k],0)+1
        
        for key, value in store.items():
            if value%n!=0:
                return False
        return True