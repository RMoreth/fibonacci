"""
crie um programa onde o usario informa o numero de sequencia sde fibonacci a ser calculada.
"""


def fibo(n):
    if n == 1:
        return 1

    elif n == 2:
        return 1
    elif n <= 0:
        return None
    else:
        return fibo(n-1) + fibo(n - 2)


r = int(input("informe quantos numeros da sequencia: "))

for l in range(r):
    print(f"{l + 1} > {fibo(l + 1)}")
