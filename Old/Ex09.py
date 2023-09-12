# Exercício de fixação 9: Crie um programa que simule um caixa eletrônico.
# O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas, a saber:

# Notas disponíveis: 1, 5, 10, 50 e 100 reais.
# Valor mínimo de saque: R$ 10,00.
# Valor máximo de saque: R$ 600,00.

valor = int(input("Qual valor deseja sacar? "))
resto = valor
#Inicia número de notas em zero
n1 = n5 = n10 = n50 = n100 = 0
if valor < 10 or valor > 600:
    print("Saque menor que o valor mínimo ou excede o valor máximo.")
else:
    if resto >= 100:
        sobra = resto % 100
        n100 = int((resto - sobra) / 100)
        resto = sobra
    if resto >= 50:
        sobra = resto % 50
        n50 = int((resto - sobra) / 50)
        resto = sobra
    if resto >= 10:
        sobra = resto % 10
        n10 = int((resto - sobra) / 10)
        resto = sobra
    if resto >= 5:
        sobra = resto % 5
        n5 = int((resto - sobra) / 5)
        resto = sobra
    n1 = resto
    print("Notas de 100:", n100)
    print("Notas de 50:", n50)
    print("Notas de 10:", n10)
    print("Notas de 5:", n5)
    print("Notas de 1:", n1)