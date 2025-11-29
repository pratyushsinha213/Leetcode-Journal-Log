class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Method 1
        # count = 0
        # for i in range(low, high+1):
        #     if i % 2 == 1:
        #         count += 1
        
        # return count

        diff = high-low
        
        if diff == 0:
            if low % 2 == 0 and high % 2 == 0:
                return 0
            elif low % 2 == 1 and high % 2 == 1:
                return 1

        if low % 2 == 0 and high % 2 == 0:
            return diff // 2
        elif low % 2 == 1 and high % 2 == 1:
            return (diff // 2) + 1
        elif low % 2 == 0 and high % 2 == 1:
            return (diff // 2) + 1
        elif low % 2 == 1 and high % 2 == 0:
            return (diff // 2) + 1