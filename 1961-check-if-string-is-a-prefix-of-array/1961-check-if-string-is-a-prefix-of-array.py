class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix_arr = []
        for i in range(len(words)):
            prefix_arr = words[0:i+1]
            if s == ''.join(prefix_arr):
                return True

        return ''.join(prefix_arr) == s