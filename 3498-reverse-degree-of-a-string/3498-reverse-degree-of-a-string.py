class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            idx = i+1
            char_idx = abs(ord(s[i]) - ord('z') - 1)
            total += (char_idx * idx)

        return total