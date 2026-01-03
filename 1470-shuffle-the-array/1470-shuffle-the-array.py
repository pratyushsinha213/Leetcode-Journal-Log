class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_arr = nums[:n]       
        y_arr = nums[n:]

        result = []

        for i in range(n):
            result.append(x_arr[i])
            result.append(y_arr[i])
        
        return result