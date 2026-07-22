class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        arr=[]
        
        word=""
        for i in range(len(s)):
            if s[i]!=" ":
                word+=s[i]
            else:
                if word != "":
                    arr.append(word)
                    word = ""
                
        if word !="":
            arr.append(word)
        
        
        return len(arr[-1])