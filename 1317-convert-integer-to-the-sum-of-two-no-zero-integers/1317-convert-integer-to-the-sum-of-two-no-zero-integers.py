class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n+1):
            a, b = str(i), str(n-i)
            if '0' not in a and '0' not in b:
                return [i, n-i]
