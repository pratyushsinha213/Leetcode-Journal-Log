# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
#         def is_palindrome(s):
#             return s == s[::-1]

#         seen = set()
#         n = len(s)
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     substr = s[i] + s[j] + s[k]
#                     if is_palindrome(substr):
#                         seen.add(substr)

#         return len(list(seen))

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        
        for ch in set(s):
            left = s.find(ch)
            right = s.rfind(ch)
            
            if left < right:
                res += len(set(s[left + 1:right]))
        
        return res