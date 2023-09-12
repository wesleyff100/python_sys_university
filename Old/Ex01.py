# Exercício de fixação 1: Crie um programa que pergunte a idade do usuário. Caso seja maior de idade, deve mostrar uma mensagem informando que pode se inscrever para 
# fazer o teste para tirar a carteira de motorista.

idade = int(input("Insira a sua idade: "))
maioridade = 18

if idade > maioridade:
    print(f"Sua idade é {idade}, já está apto a realizar o teste para tirar a carteira de motorista")
else:
    print(f"Sua idade é {idade}, não está apto a realizar o teste para tirar a carteira de motorista")
