class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s_digits = 0
        str_num = str(x)

        for num in str_num:
            s_digits += int(num)
        
        if x % s_digits == 0:
            return s_digits
        
        return -1