class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        encrypted_sum = 0

        for i in range(len(nums)):
            str_num = str(nums[i])
            digits = [int(d) for d in str_num]
            max_digit = str(max(digits))
            encrypted_sum += (int(max_digit * len(str_num)))

        return encrypted_sum