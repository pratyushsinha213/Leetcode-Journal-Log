from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def prime(n):
            if n == 1:
                return False

            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False
            
            return True

        counter = Counter(nums)
        for num, freq in counter.items():
            if prime(freq):
                print(freq)
                return True
        
        return False