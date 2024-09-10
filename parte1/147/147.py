import sys

CURRENCIES = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

def contar_combinaciones(valor):
    arreglo = [0]*(valor+1)
    arreglo[0] = 1

    for currency in CURRENCIES:
        for subtotal in range(currency, valor+1):
            arreglo[subtotal] += arreglo[subtotal - currency]

    return arreglo[valor]

def main():
    output = []
    valor = float(sys.stdin.readline().strip())
    
    while valor != 0:
        cantidad = contar_combinaciones(int(round(valor * 100, 0)))
        resultado = f"{valor:>6.2f}{cantidad:>17}"
        print(resultado)
        output.append(resultado)
        valor = float(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()
