# Agora, e se existisse mais uma decisão a ser feita? Nem tudo na vida possui somente duas escolhas, não é? Existem casos em que podemos ter três, quatro ou mais comparações. É para casos assim que temos as seleções encadeadas. Portanto, a seleção encadeada é utilizada quando existe mais de uma condição a ser avaliada na tomada de decisão. Neste caso, deve ser usado mais de um comando se aninhado.

print("Por favor, insira três números diferentes:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verificando se os números são diferentes
if num1 == num2:
    print("Os números inseridos não são diferentes.")
else:
    if num1 == num3:
        print("Os números inseridos não são diferentes.")
    else:
        if num2 == num3:
            print("Os números inseridos não são diferentes.")
        else:
            menor = num1
            if num2 < menor:
                menor = num2
            if num3 < menor:
                menor = num3

            print(f"O menor número é: {menor}")

# versão reduzida com operadores logicos : and, or, not
# print("Por favor, insira três números diferentes:")
#num1 = float(input("Digite o primeiro número: "))
#num2 = float(input("Digite o segundo número: "))
#num3 = float(input("Digite o terceiro número: "))
#if num1 == num2 or num1 == num3 or num2 == num3:
#    print("Os números inseridos não são diferentes.")
#else:
#    if num1 < num2 and num1 < num3:
#        print("O menor número é:", num1)
#    elif num2 < num3:
#        print("O menor número é:", num2)
#    else:
#        print("O menor número é:", num3)