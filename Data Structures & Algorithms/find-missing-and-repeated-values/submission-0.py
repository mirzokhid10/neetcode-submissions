class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        store={}
        counter=0
        for i in range(len(grid)):
            for k in range(len(grid[i])):
                store[grid[i][k]] = store.get(grid[i][k], 0) + 1
                counter+=1
                
        full=set(range(1,counter+1))
        store_list=set(list(store.keys()))
        
        repeated = [key for key, value in store.items() if value == 2][0]
       
        missing_n = list(full - store_list)[0]
       
        return [repeated, missing_n]