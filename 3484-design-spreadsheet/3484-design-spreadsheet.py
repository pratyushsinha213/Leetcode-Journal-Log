class Spreadsheet:

    def __init__(self, rows: int):
        self.matrix = [[0] * 26 for _ in range(rows)]

    def _get_rows_cols(self, cell):
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        return [col, row]

    def _get_cell_value(self, cell: str) -> int:
        col, row = self._get_rows_cols(cell)
        return self.matrix[row][col]

    def setCell(self, cell: str, value: int) -> None:
        col, row = self._get_rows_cols(cell)
        self.matrix[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = self._get_rows_cols(cell)
        self.matrix[row][col] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')

        val1 = int(a) if a.isnumeric() else self._get_cell_value(a)
        val2 = int(b) if b.isnumeric() else self._get_cell_value(b)

        return val1 + val2