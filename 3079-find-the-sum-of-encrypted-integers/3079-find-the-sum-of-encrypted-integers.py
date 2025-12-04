class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        encrypted = []

        for i in range(len(nums)):
            str_num = str(nums[i])
            digits = [int(d) for d in str_num]
            max_digit = str(max(digits))
            encrypted.append(int(max_digit * len(str_num)))
        
        print(encrypted)
        return sum(encrypted)