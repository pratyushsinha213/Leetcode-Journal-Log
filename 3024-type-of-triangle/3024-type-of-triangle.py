class Solution:
    def triangleType(self, nums: List[int]) -> str:
        def check_if_tngle(arr):
            a, b, c = arr
            if a + b > c and b + c > a and a + c > b:
                return True
            return False

        tngle_check = set(nums)

        if len(tngle_check) == 1:
            return "equilateral"
        elif check_if_tngle(nums) and len(tngle_check) == 2:
            return "isosceles"
        else:
            if check_if_tngle(nums) and len(tngle_check) == 3:
                return "scalene"
            else:
                return "none"