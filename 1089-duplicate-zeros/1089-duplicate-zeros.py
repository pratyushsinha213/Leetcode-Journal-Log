class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if 0 not in arr:
            return arr

        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 2
            else:
                i += 1
            
        arr[:] = arr[:n]


        '''
                  n = 7
                  i = 0 1 2 3 4 5 6
                arr = 1 0 2 3 0 4 5
        
        '''