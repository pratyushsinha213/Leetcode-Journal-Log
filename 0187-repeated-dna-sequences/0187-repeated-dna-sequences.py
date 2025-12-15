class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(9, len(s)):
            sub_str = s[i-9:i+1]
            if sub_str in seen:
                res.add(sub_str)
            else:
                seen.add(sub_str)
        
        return list(res)