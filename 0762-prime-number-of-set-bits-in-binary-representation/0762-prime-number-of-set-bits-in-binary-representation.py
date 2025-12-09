class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            bin_n = bin(n)[2:]
            count_1s = bin_n.count("1")
            if count_1s == 1:
                return False
            for i in range(2, count_1s):
                if count_1s % i == 0:
                    return False            
            return True

        count = 0
        for i in range(left, right+1):
            if is_prime(i):
                count += 1
        
        return count