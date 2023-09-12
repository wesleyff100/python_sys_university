# Exercício de fixação 2: Crie um programa que pergunte o nome do cliente para ser inserido em um cartão de crédito, com espaço máximo de 20 caracteres.
# Caso o usuário informe um nome maior, deve mostrar uma mensagem informando que o nome é extenso demais e deve ser abreviado.
# Dica: para saber o tamanho de uma string, usar a função len. Exemplo: len(nome).

nome_cliente = str(input("Insira o seu nome(maximo 20 caracteres): "))
if len(nome_cliente) > 20:
    print("O Nome possui mais de 20 caracteres")
else:
    print("Entrou")
