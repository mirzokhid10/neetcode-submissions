class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store={}
        for i in range(len(strs)):
            a="".join(sorted(strs[i]))
            if a not in store:
                store[a]=[]
                
            store[a].append(strs[i])
        return list(store.values())