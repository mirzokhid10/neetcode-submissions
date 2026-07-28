class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq={}
        counter=0
        for i in chars:
            freq[i]=freq.get(i,0)+1
        
        for k in range(len(words)):
            count={}
            for m in range(len(words[k])):
                count[words[k][m]]=count.get(words[k][m],0)+1
            
    
            can_form = True
            for letter, letter_count in count.items():
                if freq.get(letter, 0) < letter_count:
                    can_form = False
                    break
            
            if can_form:
                counter += len(words[k])
                
        return counter