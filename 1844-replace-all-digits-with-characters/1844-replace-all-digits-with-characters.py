class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(alpha, number):
            return chr(ord(alpha) + int(number))
        i = 0
        s_arr = [char for char in s]
        while i < len(s_arr):
            if i%2 == 0:
                i += 1
                continue
            
            s_arr[i] = shift(s_arr[i-1], s_arr[i])
            i += 1
        
        return ''.join(s_arr)