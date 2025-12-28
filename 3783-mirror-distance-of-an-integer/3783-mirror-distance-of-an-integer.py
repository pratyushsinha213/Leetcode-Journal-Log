class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        temp = n
        while temp > 0:
            rem = temp % 10
            temp = temp // 10
            rev = rev * 10 + rem

        return abs(n-rev)