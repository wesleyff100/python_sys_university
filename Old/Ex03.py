# Exercício de fixação 3: Crie um programa que solicite um número ao usuário e informe se é par ou ímpar.
# Dica: para saber se um número é par ou ímpar, calcular o resto da divisão desse número por 2 (operador %).
# Se o resultado for 0, o número será par; se for 1, será ímpar.

numero = int(input("Insira um numero: "))
if numero % 2 == 0 :
    print(f"O Numero {numero} é par")
else:
    print(f"O Numero {numero} é impar")