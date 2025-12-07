class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        non_zero = []
        concat = []
        str_n = str(n)

        for i in range(len(str_n)):
            if str_n[i] != "0":
                non_zero.append(int(str_n[i]))
                concat.append(str_n[i])
        
        sum_digits = sum(non_zero)
        
        return int(''.join(concat)) * sum_digits