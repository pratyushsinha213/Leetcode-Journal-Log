class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()

        while nums:
            nums.sort()

            minn = nums[0]
            maxx = nums[-1]
            average = (maxx + minn) / 2
            avg.add(average)
            
            # print(f"min: {minn}, max: {maxx}")

            nums = nums[1:len(nums)-1]

            # print(f"new_nums: {nums}")
        
        return len(list(avg))