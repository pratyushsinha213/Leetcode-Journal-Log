class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        str_1, str_2, str_3 = str(num1), str(num2), str(num3)
        max_len = max(len(str_1), len(str_2), len(str_3))

        str_1 = '0' * (max_len - len(str_1)) + str_1
        str_2 = '0' * (max_len - len(str_2)) + str_2
        str_3 = '0' * (max_len - len(str_3)) + str_3

        key = []

        for i in range(max_len):
            least = min(int(str_1[i]), int(str_2[i]), int(str_3[i]))
            key.append(str(least))
        
        return int(''.join(key))