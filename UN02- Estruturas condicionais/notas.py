nota1 = float(input(" Digite a Primeira nota: "))
nota2 = float(input(" Digite a Segunda nota: "))
nota3 = float(input(" Digite a Terceira nota: "))
nota4 = float(input(" Digite a Quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
media_passar = 7
if media >= media_passar:
    print(f"O estudante foi aprovado com uma média de {media}")
else:
     print(f"O estudante não atingiu a média, com a nota de {media}")
