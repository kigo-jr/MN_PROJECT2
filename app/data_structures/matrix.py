from typing import List, Union
from data_structures.vector import vector


class matrix:

    """
    Klasa reprezentująca macierz.
    """

    def __init__(self, array: Union[List[List[float]], None]=None) -> None:
        if array is None:
            self.matrix = [[float("nan")]]
        else:
            self.matrix = array

    def __str__(self) -> str:
        str_representation: str = ""
        for row in self.matrix:
            str_representation += "| "
            for element in row:
                str_representation += f"{element:10.4f} "
            str_representation += "|\n"
        return str_representation

    def __eq__(self, __o: object) -> bool:
        if type(__o) != type(self) or self.cols != __o.cols or self.rows != __o.rows:
            return False

        try:
            for i in range(self.rows):
                for j in range(self.cols):
                    if __o.matrix[i][j] != self.matrix[i][j]:
                        raise Exception
        except Exception:
            return False

        return True

    def __getitem__(self, key: int) -> List[float]:
        return self.matrix[key]

    def __add__(self, __o: "matrix") -> "matrix":
        if  self.rows != __o.rows or self.cols != __o.cols:
            raise Exception("Matrices have to be of equal size in order to add them!")

        addition_list: List[List[float]] = self.copy().matrix
        other_list: List[List[float]] = __o.copy().matrix

        for i in range(len(addition_list)):
            for j in range(len(addition_list[0])):
                addition_list[i][j] += other_list[i][j]

        return matrix(addition_list)

    def __sub__(self, __o: "matrix") -> "matrix":
        if  self.rows != __o.rows or self.cols != __o.cols:
            raise Exception("Matrices have to be of equal size in order to subtract them!")

        subtraction_list: List[List[float]] = self.copy().matrix
        other_list: List[List[float]] = __o.copy().matrix

        for i in range(len(subtraction_list)):
            for j in range(len(subtraction_list[0])):
                subtraction_list[i][j] -= other_list[i][j]

        return matrix(subtraction_list)

    def __mul__(self, __o: Union["matrix", vector]) -> Union["matrix", vector]:
        # TODO: implement dot product of matrices and matrix with vector

        self_copy: matrix = self.copy()
        other_copy: Union["matrix", vector] = __o.copy()

        if type(__o) == type(self):
            # HACK: TBH it's not needed in this project!
            pass
        elif isinstance(__o, vector):
            if self_copy.cols != len(__o):
                raise Exception("Objects of not compatible sizes!")

            return_vector: vector = vector([0.0 for _ in range(self_copy.rows)])

            for i in range(self_copy.rows):
                for j in range(self_copy.cols):
                    return_vector.vector[i] += self_copy.matrix[i][j]*other_copy.vector[j]

            return return_vector

    @property
    def matrix(self) -> List[List[float]]:
        return self._matrix

    @matrix.setter
    def matrix(self, matrix: List[List[float]]) -> None:
        rows: int = len(matrix)

        if rows > 0 and matrix[0][0] == float("nan"):
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

    def copy(self) -> "matrix":
        copy_list = [[element for element in row] for row in self.matrix]
        return matrix(copy_list)
