class Solution:
    def countAsterisks(self, s: str) -> int:
        if "*" not in s:
            return 0
        
        split_s = s.split("|")
        count = 0
        for i in range(0, len(split_s), 2):
            count += split_s[i].count("*")
        
        return count