class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0
        
        bin_n, bin_k = bin(n)[2:], bin(k)[2:]

        if len(bin_n) < len(bin_k):
            bin_n = '0' * (len(bin_k)-len(bin_n)) + bin_n
        elif len(bin_k) < len(bin_n):
            bin_k = '0' * (len(bin_n)-len(bin_k)) + bin_k

        changes = 0
        for a, b in zip(bin_n, bin_k):
            if a == '0' and b == '1':
                return -1  # impossible
            if a == '1' and b == '0':
                changes += 1
        
        return changes