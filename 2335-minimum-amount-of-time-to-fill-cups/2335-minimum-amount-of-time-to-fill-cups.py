class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        amount.sort()

        while amount[1] and amount[2]:
            ans += 1

            amount[1] -= 1
            amount[2] -= 1

            amount.sort()

        ans += amount[2]

        return ans