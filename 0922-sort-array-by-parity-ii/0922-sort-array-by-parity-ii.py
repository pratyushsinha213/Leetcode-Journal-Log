class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_arr, odd_arr = [], []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_arr.append(nums[i])
            else:
                odd_arr.append(nums[i])
        
        even_arr.sort()
        odd_arr.sort()

        result = [None] * len(nums)
        ei, oi = 0, 0
        for i in range(len(result)):
            if i % 2 == 0:
                if ei < len(even_arr):
                    result[i] = even_arr[ei]
                    ei += 1
            else:
                if oi < len(odd_arr):
                    result[i] = odd_arr[oi]
                    oi += 1
        
        return result
