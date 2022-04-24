from math import sin
import matplotlib.pyplot as plt
from data_structures import vector, matrix
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

# TODO: a_1 = 5 + 4, N = 969, b_n = sin(n*(2+1))

if __name__ == "__main__":

    #  zadanie A
    #  indeks: 172469
    #  N = 969, a1 = 9, a2 = a3 = -1, bn = sin(n*3)

    N = 969
    b = vector([sin((i + 1) * 3) for i in range(N)])
    A = matrix([
        [9 if i==j else -1 if j < i+3 and i < j+3 else 0 for i in range(N)] for j in range(N)
    ])

    #  zadanie B

    time, iters, solution, residuum = A.jacobi(b)
    print("Jacobi's method:")
    print(f"residuum norm: {residuum.norm}")
    print(f"needed iterations: {iters}")
    print(f"execution time: {time} s.")

    time, iters, solution, residuum = A.gauss_seidel(b)
    print("Gauss-Seidel's method:")
    print(f"residuum norm: {residuum.norm}")
    print(f"needed iterations: {iters}")
    print(f"execution time: {time} s.")

    # zadanie C

    b = vector([sin((i + 1) * 3) for i in range(N)])
    A = matrix([
        [3 if i==j else -1 if j < i+3 and i < j+3 else 0 for i in range(N)] for j in range(N)
    ])

    try:
        time, iters, solution, residuum = A.jacobi(b)
    except Exception:
        print("Jacobi's method did not converge!")

    try:
        time, iters, solution, residuum = A.gauss_seidel(b)
    except Exception:
        print("Gauss-Seidel's method did not converge!")

    # zadanie D

    time, solution, residuum = A.lu_factorization(b)
    print("LU factorization:")
    print(f"residuum norm: {residuum.norm}")
    print(f"execution time: {time} s.")

    # zadanie E

    N_vector = [100, 500, 1000, 2000, 3000]

    Jacobi_times = []
    Gauss_Seidels_times = []
    LU_factorization_times = []

    for n in N_vector:
        b = vector([sin((i + 1) * 3) for i in range(n)])
        A = matrix([
            [9 if i==j else -1 if j < i+3 and i < j+3 else 0 for i in range(n)] for j in range(n)
        ])

        Jacobi_times.append(A.jacobi(b)[0])
        Gauss_Seidels_times.append(A.gauss_seidel(b)[0])
        LU_factorization_times.append(A.lu_factorization(b)[0])

    plt.plot(N_vector, Jacobi_times, label="Jacobi", color="red")
    plt.plot(N_vector, Gauss_Seidels_times, label="Gauss-Seidel", color="blue")
    plt.plot(N_vector, LU_factorization_times, label="LU factorization", color="green")
    plt.grid(True)
    plt.legend()
    plt.ylabel(r"Czas [$s$]")
    plt.xlabel("Liczba niewiadomych")
    plt.title("Zależność czasu wykonywania algorytmów od liczby niewiadomych")
    plt.show()
