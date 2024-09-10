from sys import stdin

def maxima_ganancia(n_apuestas: int, apuestas: list[int]) -> int:
    arreglo = [0]*n_apuestas
    arreglo[0] = apuestas[0]
    ganancia_maxima = arreglo[0]

    for i in range(1, n_apuestas):
        arreglo[i] = max(apuestas[i], arreglo[i-1] + apuestas[i])
        ganancia_maxima = max(ganancia_maxima, arreglo[i])

    return ganancia_maxima

def main():
    n_apuestas = int(stdin.readline().strip())
    while n_apuestas != 0:
        apuestas = list(map(int, stdin.readline().split()))
        ganancia_maxima = maxima_ganancia(n_apuestas, apuestas)

        if ganancia_maxima > 0:
            print("The maximum winning streak is " + str(ganancia_maxima) + ".")

        else:
            print("Losing streak.")
        n_apuestas = int(stdin.readline().strip())

if __name__ == '__main__':
    main()