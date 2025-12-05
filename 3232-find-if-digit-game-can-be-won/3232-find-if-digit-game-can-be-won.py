class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        def choose_all_single_digits(arr):
            alice, bob = 0, 0
            for num in arr:
                if num < 10:
                    alice += num
                else:
                    bob += num
            
            return alice > bob
        
        def choose_all_double_digits(arr):
            alice, bob = 0, 0
            for num in arr:
                if num < 10:
                    bob += num
                else:
                    alice += num
            
            return alice > bob
        
        return choose_all_single_digits(nums) | choose_all_double_digits(nums)