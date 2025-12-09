class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_arr, odd_arr = [], []

        for num in nums:
            if num % 2 == 0:
                even_arr.append(num)
            else:
                odd_arr.append(num)

        return even_arr + odd_arr