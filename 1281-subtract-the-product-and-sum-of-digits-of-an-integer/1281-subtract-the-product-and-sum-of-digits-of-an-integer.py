class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, summ = 1, 0

        for num in str(n):
            prod *= int(num)
            summ += int(num)
        
        return prod - summ