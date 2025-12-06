class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = len(fruits)
        used = [False] * len(baskets)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j] and not used[j]:
                    baskets[j] -= fruits[i]
                    count -= 1
                    used[j] = True
                    break
        
        return count