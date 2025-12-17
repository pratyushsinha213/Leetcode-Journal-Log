class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(rem):
            if rem < 0:
                return float('inf')
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + dp(rem - coin))

            memo[rem] = min_coins
            return min_coins

        result = dp(amount)
        return result if result != float('inf') else -1