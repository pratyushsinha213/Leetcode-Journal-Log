class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        if len(nums) == 1:
            if indexDifference <= 0:
                if abs(nums[0] - nums[0]) >= valueDifference:
                    return [0, 0]
                else:
                    return [-1, -1]

        left, right = 0, len(nums)-1
        answer = [-1, -1]

        # while left < right:
        #     if abs(left -right) >= indexDifference:
        #         if abs(nums[left] - nums[right]) >= valueDifference:
        #             answer = [left, right]
            
        #     left += 1
        #     right -= 1

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                    if abs(i -j) >= indexDifference:
                        if abs(nums[i] - nums[j]) >= valueDifference:
                            answer = [i, j]
        
        return answer