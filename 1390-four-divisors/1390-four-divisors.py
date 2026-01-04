# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         def has_four_divisors(n):
#             count = 2
#             add = 1+n
#             for i in range(2, n):
#                 if count > 4:
#                     return False, 0
#                 if n % i == 0:
#                     count += 1
#                     add += i
            
#             return count == 4, add 
        
#         result = 0
#         for num in nums:
#             is_true, add = has_four_divisors(num)
#             if is_true:
#                 result += add

#         return result

class Solution:
    def get_divisors(self, n):

        divisors = []
        limit = n ** 0.5
        i = 1
        while(i <= limit):

            if(n % i == 0):
                divisors.append(i)
                
                poss_div = n//i
                if(poss_div != i):
                    divisors.append(poss_div)

            i += 1
        
        return divisors
    
    def sumFourDivisors(self, nums: list[int]) -> int:
        
        ans = 0
        for num in nums:
            divisors = self.get_divisors(num)

            if(len(divisors) == 4):
                ans += sum(divisors)
        
        return ans
        