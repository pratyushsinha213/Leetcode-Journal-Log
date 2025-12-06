class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        time_x, time_y = abs(x-z), abs(y-z)
        
        if time_y > time_x:
            return 1
        elif time_x > time_y:
            return 2
        else:
            return 0