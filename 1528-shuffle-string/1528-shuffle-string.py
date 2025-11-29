class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [char for char in s]
        index = dict()

        for i in range(len(ans)):
            index[indices[i]] = ans[i]

        result = []
        for i in range(len(ans)):
            result.append(index[i])
        
        return ''.join(result)