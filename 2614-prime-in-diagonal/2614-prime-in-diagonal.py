class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        diagonals = []
        seen = set()

        m, n = len(nums), len(nums[0])

        for i in range(m):
            for j in range(n):
                if (i == j or i + j == m-1) and (i, j) not in seen:
                    diagonals.append(nums[i][j])
                    seen.add((i, j))
        
        # print(diagonals)

        primes = set()
        for num in diagonals:
            if is_prime(num):
                primes.add(num)
            
        return max(primes) if primes else 0