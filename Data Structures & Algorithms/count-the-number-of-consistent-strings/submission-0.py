class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set=set()    
        counter=0
        arrs=[]
    
        for i in range(len(allowed)):
            allowed_set.add(allowed[i])
        
        allowed_set=list(allowed_set)
        allowed_set.sort()
        print(allowed_set)
        
        for word in words:
            words_set=set()
            for k in range(len(word)):
                words_set.add(word[k])
                
            words_set=list(words_set)
            words_set.sort()
            print(words_set)
            
            is_consistent = True
            for letter in words_set:
                if letter not in allowed_set:
                    is_consistent = False
                    break
                
            if is_consistent:
                counter += 1
    
    
        return counter