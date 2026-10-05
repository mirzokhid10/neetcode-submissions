class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for str in strs:
            s = "".join(sorted(str))
    
            if s not in store:
                store[s] = []
            store[s].append(str)
    
        return list(store.values())