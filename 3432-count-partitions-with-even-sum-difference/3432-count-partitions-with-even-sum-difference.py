class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        partition_count = 0
        for i in range(len(nums)-1):
            left_arr_sum = sum(nums[:i+1])
            right_arr_sum = sum(nums[i+1:])

            if (left_arr_sum - right_arr_sum) % 2 == 0:
                partition_count += 1
            
        return partition_count