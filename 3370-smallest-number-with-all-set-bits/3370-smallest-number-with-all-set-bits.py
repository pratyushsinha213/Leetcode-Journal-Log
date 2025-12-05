class Solution:
    def smallestNumber(self, n: int) -> int:
        while True:
            bin_rep = bin(n)[2:]
            if '0' not in bin_rep:
                return n
            else:
                n += 1