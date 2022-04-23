from typing import List, Tuple, Union
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
                str_representation += f"{element:10.4e} "
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
                raise Exception(f"Objects of not compatible sizes! (vector of length {len(__o)} and matrix of {self_copy.cols} columns)")

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

    @staticmethod
    def ones(n: int) -> "matrix":
        return matrix([[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)])

    def copy(self) -> "matrix":
        copy_list = [[element for element in row] for row in self.matrix]
        return matrix(copy_list)

    def jacobi(self, b: vector, inplace: bool=False) -> Tuple[float, int, vector]:
        if self.cols != len(b):
            raise Exception("")

        A_copy: "matrix" = self.copy() if not inplace else self

        iterations: int = 0

        x: vector = vector.ones(len(b))
        tmp_x: vector = x.copy()

        while True:
            for i in range(A_copy.rows):
                value: float = b[i]
                # TODO: make sure it really is Jacobi's method
                value -= sum([A_copy[i][j] * x[j] for j in range(A_copy.cols) if i != j])
                value /= A_copy[i][i]
                tmp_x[i] = value

            x = tmp_x.copy()
            res: vector = A_copy * x - b

            iterations += 1

            if res.norm < 1e-9:
                break
        # TODO: measure time in Jacobi's method
        return (0.0, iterations, x)

    def gauss_seidl(self, b: vector, inplace: bool=False) -> Tuple[float, int, vector]:
        if self.cols != len(b):
            raise Exception("")

        A_copy: "matrix" = self.copy() if not inplace else self

        iterations: int = 0

        x: vector = vector.ones(len(b))

        while True:
            for i in range(A_copy.rows):
                value: float = b[i]
                # TODO: make sure it really is Gauss Seidel's method
                value -= sum([A_copy[i][j] * x[j] for j in range(A_copy.cols) if i != j])
                value /= A_copy[i][i]
                x[i] = value

            res: vector = A_copy * x - b

            iterations += 1

            if res.norm < 1e-9:
                break
        # TODO: measure time in Gauss Seidel's method
        return (0.0, iterations, x)

    def lu_factorization(self, b: vector, inplace: bool=False) -> Tuple[float, int, vector]:
        # TODO: implement LU factorization
        pass
