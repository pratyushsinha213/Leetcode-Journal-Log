class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(n):
            str_n = str(n)
            for digit in str_n:
                if int(digit) == 0 or n % int(digit) != 0:
                    return False
            return True

        arr = []
        for num in range(left, right+1):
            if is_self_dividing(num):
                arr.append(num)

        return arr