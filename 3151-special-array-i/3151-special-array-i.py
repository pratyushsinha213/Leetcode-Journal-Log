class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        # Method 1
        
        # odd_parity = [False] * len(nums)
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 1:
        #         odd_parity[i] = True

        # for i in range(len(odd_parity)-1):
        #     if (odd_parity[i] and odd_parity[i+1]) or (not odd_parity[i] and not odd_parity[i+1]):
        #         return False
            
        # return True

        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:
                return False
        
        return True