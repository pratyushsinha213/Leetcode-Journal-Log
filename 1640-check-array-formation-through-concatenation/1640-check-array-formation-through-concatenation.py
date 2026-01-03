class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = {}
        res = []

        for piece in pieces:
            mapping[piece[0]] = piece
        
        for i in arr:
            if i in mapping:
                res += mapping[i]

        return res == arr