class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []

        for i in range(len(matrix)):
            arr.extend(matrix[i])
            # for j in range(len(matrix[0])):
        
        # print(arr)
        arr.sort()
        return arr[k-1]