import matplotlib.pyplot as plt
from data_structures import vector, matrix

# TODO: a_1 = 5 + 4, N = 969, b_n = sin(n*(2+1))

if __name__ == "__main__":
    A = matrix([
        [1.5, 1.1, -0.3],
        [1.1, 1.5, 1.1],
        [0.3, 1.1, 2.0]
    ])

    x = vector(
        [-4.025, 5.825, -2.10]
    )

    v = vector([1, 1, 0])

    time, iters, solution = A.jacobi(vector([1.0, 2.0, 1.0]))
    print("Jacobi method:")
    print(A * solution)
    print(f"solution:\n{solution}")
    print(f"needed iterations: {iters}")

    time, iters, solution = A.gauss_seidl(vector([1.0, 2.0, 1.0]))
    print("Gauss Seidel method:")
    print(A * solution)
    print(f"solution:\n{solution}")
    print(f"needed iterations: {iters}")
