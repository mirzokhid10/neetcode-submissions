class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq = {}
        for s in students:
            freq[s] = freq.get(s, 0) + 1
        
        for sandwich in sandwiches:
            if freq.get(sandwich, 0) > 0:
                freq[sandwich] -= 1
            else:
                return freq.get(0, 0) + freq.get(1, 0)
        
        return 0