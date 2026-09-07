"""Módulo para calcular e imprimir números primos inferiores a 100."""
import math

def is_prime(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    """Contém toda a lógica principal."""
    for i in range(100):
        if is_prime(i):
            print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
