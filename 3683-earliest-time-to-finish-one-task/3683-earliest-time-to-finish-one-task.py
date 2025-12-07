class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        least = float('inf')

        for task in tasks:
            time = sum(task)
            print(time)
            if time < least:
                least = time
        
        return least