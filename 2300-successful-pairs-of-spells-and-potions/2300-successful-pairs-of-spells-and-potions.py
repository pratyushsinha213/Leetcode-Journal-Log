# class Solution:
#     def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
#         dp = {}
#         n, m = len(spells), len(potions)
#         arr = []
#         for i in range(n):
#             spell = spells[i]
#             if spell in dp:
#                 arr.append(dp[spell])
#                 continue
#             temp = [num * spell for num in potions]
#             count = 0
#             for strength in temp:
#                 if strength >= success:
#                     count += 1
            
#             arr.append(count)
#             dp[spell] = count
        
#         return arr

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            # Minimum potion needed
            need = (success + spell - 1) // spell  # ceiling division
            idx = bisect_left(potions, need)
            result.append(m - idx)

        return result