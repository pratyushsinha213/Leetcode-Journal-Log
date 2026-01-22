class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def isSorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        ops = 0

        while not isSorted(nums):
            min_sum = float("inf")
            idx = 0

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < min_sum:
                    min_sum = nums[i] + nums[i + 1]
                    idx = i

            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1

        return ops