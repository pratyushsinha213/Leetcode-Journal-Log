class Solution:
    def scoreBalance(self, s: str) -> bool:

        for i in range(len(s)-1):
            left, right = s[:i+1], s[i+1:]
            score_l, score_r = 0, 0
            for j in range(len(left)):
                score_l += (ord(left[j]) - ord('a') + 1)
            for k in range(len(right)):
                score_r += (ord(right[k]) - ord('a') + 1)

            if score_l == score_r:
                return True
        
        return False