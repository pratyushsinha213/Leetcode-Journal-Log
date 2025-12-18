class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        counter_p = Counter(p)
        arr = []
        for i in range(len(s) - len(p) + 1):
            sub_str = s[i:i+len(p)]
            counter_sub = Counter(sub_str)
            if counter_sub == counter_p:
                arr.append(i)

        return arr