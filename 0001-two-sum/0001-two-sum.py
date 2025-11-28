class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Time : O(N^2)'''
        newList = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target and len(newList) == 0):
                    newList.append(i)
                    newList.append(j)
        
        return newList