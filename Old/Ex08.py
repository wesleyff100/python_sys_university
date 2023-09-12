# Exercício de fixação 8: Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria e o número de faltas.
# Informe se o aluno foi aprovado ou reprovado, bem como o motivo, a saber:

# A média anual é 7.
# A disciplina possui 40 aulas.
# O mínimo exigido é 75% de presença.

print("Digite as quatro notas bimestrais da disciplina: ")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
faltas = int(input("Digite o número de faltas: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua média na disciplina foi", media)
pres = 100 - (faltas * 100) / 40
print("Sua porcentagem de presença é de", pres, "%")
if media >= 7 and pres >= 75:
    print("Você está aprovado na disciplina!")
elif media >= 7 and pres < 75:
    print("Você foi reprovado por faltas!")
elif media <=7 and pres >= 75:
    print("Você foi reprovado por nota!")
else:
    print("Você foi reprovado por nota e por faltas!")