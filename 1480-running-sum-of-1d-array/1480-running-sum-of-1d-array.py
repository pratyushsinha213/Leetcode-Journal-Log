class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        answer = [0] * len(nums)

        for i in range(len(nums)):
            curr_sum += nums[i]
            answer[i] = curr_sum
        
        return answer