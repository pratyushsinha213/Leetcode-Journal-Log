class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        averages = []

        for i in range(len(nums)):
            if len(nums) != 0:
                max_elem = nums[-1]
                min_elem = nums[0]

                averages.append((max_elem + min_elem)/2)

                nums = nums[1:len(nums)-1]
        
        return min(averages)