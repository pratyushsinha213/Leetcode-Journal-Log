class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = ''
        for ch in s:
            num_str += str(ord(ch)-ord('a')+1)

        while k > 0:
            str_sum = 0
            for num in num_str:
                str_sum += int(num)
            
            num_str = str(str_sum)
            k -= 1

        return int(num_str)