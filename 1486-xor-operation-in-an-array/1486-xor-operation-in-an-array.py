class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0] * n
        xor_ops = 0

        for i in range(n):
            nums[i] = start + (2 * i)
            xor_ops ^= nums[i]
        
        return xor_ops