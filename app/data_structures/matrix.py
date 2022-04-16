import numpy as np

class Matrix:

    """
    Klasa reprezentująca macierz.
    """

    def __init__(self) -> None:
        self.matrix = np.array(np.nan)

    def __init__(self, array: np.array) -> None:
        self._matrix = array


    @property
    def matrix(self) -> np.array:
        return self._matrix

    @matrix.setter
    def matrix(self, matrix: np.array) -> None:
        rows: int = len(matrix)

        if rows > 0 and matrix[0] == np.nan:
            rows = 0

        cols: int = 0
        if rows > 0:
            cols = len(matrix[0])

        for row in matrix:
            if len(row) != cols:
                raise Exception("Rows do not have equal length")

        self._matrix = matrix
        self._cols = cols
        self._rows = rows

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols
