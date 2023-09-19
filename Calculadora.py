"""
Primeiro Programa (calculadora simples)
"""
op = input("""Digite a operação que deseja fazer:
+ para Adição
- para Subtração
* para Multiplicação
/ para Divisão
""")

n1 = int(input("Introduza o primeiro número"))
n2 = int(input("Introduza o segundo número"))

# Adição
if op == "+":
    print('{} + {} = '.format(n1, n2))
    print(n1 + n2)

# Subtração
elif op == "-":
    print('{} - {} = '.format(n1, n2))
    print(n1 - n2)

# Multiplicação
elif op == "*":
    print('{} * {} = '.format(n1, n2))
    print(n1 * n2)

# Divisão
elif op == "/":
    print('{} / {} = '.format(n1, n2))
    print(n1 / n2)

else:
    print("Não escolheu uma operação válida")
