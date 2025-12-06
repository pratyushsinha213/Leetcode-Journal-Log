class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        set_f = set(friends)
        result = []

        for num in order:
            if num in set_f:
                result.append(num)
        
        return result