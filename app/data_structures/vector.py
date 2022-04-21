from typing import List

class vector:

    def __init__(self, vector: List[float]) -> None:
        self.vector = vector
        self.length = len(vector)

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        str_representation: str = ""
        for element in self.vector:
            str_representation += f"|{element:10.4f}|\n"

        return str_representation

    @property
    def norm(self) -> float:
        norm: float = 0.0
        for element in self.vector:
            norm += element ** 2

        norm **= 0.5

        return norm

    @property
    def vector(self) -> List[float]:
        return self._vector

    @vector.setter
    def vector(self, vector: List[float]) -> None:
        self._vector = vector
        self.length = len(vector)

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        self._length = length

    def copy(self) -> "vector":
        copy_list = [element for element in self.vector]
        return vector(copy_list)
