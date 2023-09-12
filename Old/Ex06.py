# Exercício de fixação 6: Crie um programa que solicite ao usuário dois números e a operação que deseja executar entre eles.
# Mostre o resultado dessa operação no formato: num1 op num2 = resultado.
num1 = int(input("Insira o Primeiro numero: "))
num2 = int(input("Insira o Segundo numero: "))
op = str(input(" Qual será a operação ( + - * / )?"))
resultado = 0

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == -"*":
    resultado = num1 * num2
elif op == - "/":
    resultado = num1 / num2
else:
    print("Operação invalida")

print(f"O resultado da operação de {num1}{op}{num2} = {resultado}")