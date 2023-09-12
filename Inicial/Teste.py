class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Disciplina:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

class Professor:
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

class Turma:
    def __init__(self, codigo, disciplina, professor):
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor

class Matricula:
    def __init__(self, estudante, turma):
        self.estudante = estudante
        self.turma = turma

def mostrar_menu_principal():
    print("Menu Principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")

def mostrar_menu_operacoes():
    print("Menu de Operações:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao Menu Principal")

estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

while True:
    mostrar_menu_principal()
    opcao_principal = input("Escolha uma opção: ")

    if opcao_principal == '1':
        while True:
            mostrar_menu_operacoes()
            opcao_operacoes = input("Escolha uma operação: ")

            if opcao_operacoes == '5':
                break

    elif opcao_principal == '2':
        while True:
            mostrar_menu_operacoes()
            opcao_operacoes = input("Escolha uma operação: ")

            if opcao_operacoes == '5':
                break

    # Continue para as outras opções do menu principal (3, 4, 5, 6)...

    elif opcao_principal == '6':
        print("Encerrando o programa.")
        break