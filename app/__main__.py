from data_structures import vector, matrix

if __name__ == "__main__":
    A = matrix([[2137, 213.7, 21.37],
                [2.137, 6969, 6969],
                [123, 321, 123]])

    v = vector([0, 1, 0])

    B = matrix()

    print(A + A)
    print(A - A)
    print(A)
    print(A * v)

    A2 = A.copy()
