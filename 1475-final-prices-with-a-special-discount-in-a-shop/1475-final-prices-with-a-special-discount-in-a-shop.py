class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        arr = []

        for i in range(len(prices)):
            dsct = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    dsct = prices[j]
                    break
            arr.append(prices[i]-dsct)
        
        return arr