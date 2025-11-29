class Solution:
    def sumBase(self, n: int, k: int) -> int:
        str_builder = ''

        while n > 0:
            str_builder += str(n % k)
            n = n // k
        
        return sum([int(num) for num in str_builder[::-1]])