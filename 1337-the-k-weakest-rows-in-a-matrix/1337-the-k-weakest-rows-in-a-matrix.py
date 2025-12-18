class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows = []
        for i in range(len(mat)):
            rows.append((mat[i].count(1), i))
        
        heapq.heapify(rows)

        arr = []
        for i in range(k):
            num_soldiers, row = heapq.heappop(rows)
            arr.append(row)

        return arr