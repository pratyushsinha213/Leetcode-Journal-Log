class Solution:
    def concatHex36(self, n: int) -> str:
        def hex_dec_to_16(num):
            digits = "0123456789ABCDEF"
            result = ""

            if num == 0:
                return "0"

            while num > 0:
                rem = num % 16
                num = num // 16
                result += digits[rem]

            return result[::-1]
        
        def hex_dec_to_36(num):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""

            if num == 0:
                return "0"

            while num > 0:
                rem = num % 36
                num = num // 36
                result += digits[rem]

            return result[::-1]

        return hex_dec_to_16(n ** 2)+hex_dec_to_36(n ** 3)
        # hex_dec_to_16(n ** 2)
        # hex_dec_to_36(n ** 3)