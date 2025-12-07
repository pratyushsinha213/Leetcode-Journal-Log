class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        least = 201

        for task in tasks:
            time = task[0] + task[1]
            print(time)
            if time < least:
                least = time
        
        return least