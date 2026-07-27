class Solution:
    def findLucky(self, arr: List[int]) -> int:
        store={}
        cub=[]
    
        for i in arr:
            store[i]=store.get(i, 0)+1
        
        print(store)
        st_k=list(store.keys())    
        st_v=list(store.values())
        
        for k in range(len(st_k)):
            if st_k[k]==st_v[k]:
                cub.append(st_k[k])
        
        return max(cub) if len(cub) > 0 else -1