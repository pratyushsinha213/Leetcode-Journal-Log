class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            str_digit = str(n)
            prod = 1            
            for i in range(len(str_digit)):
                prod *= int(str_digit[i])
            
            if prod % t == 0:
                return n
                break
            else:
                n = n+1