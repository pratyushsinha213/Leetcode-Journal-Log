class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                row_elems = [matrix[i][num] for num in range(len(matrix[i]))]
                col_elems = [matrix[a][j] for a in range(len(matrix))]
                # print(f"Elem {matrix[i][j]} : \n\tRow elems: {row_elems}, Col elems: {col_elems}")
                minn_elem, maxx_elem = min(row_elems), max(col_elems)
                if minn_elem == matrix[i][j] and maxx_elem == matrix[i][j]:
                    ans = [matrix[i][j]]
        
        return ans