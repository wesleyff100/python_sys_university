# Atividade formatica
# Conforme as orientações iniciais, o projeto envolve a criação de um   sistema para gestão de dados acadêmicos, ou seja,
# gerenciamento de dados de estudantes, disciplinas, professores, turmas e matrículas. Este tipo de sistema pode ser chamado de 
# CRUD (Create – Retrieve - Update – Delete), pois para cada um dos dados citados, desenvolveremos as funcionalidades de incluir, listar, atualizar e excluir.

# Definir os menus
def mostrar_menu_principal():
    print("Bem vindo ao menu principal")
    print("1.	Estudantes")
    print("2.	Disciplinas")
    print("3.	Professores")
    print("4.	Turmas")
    print("5.	Matrículas")
    print("0.   Sair")

def mostrar_menu_operacoes():
    print("1.	Incluir")
    print("2.	Listar")
    print("3.	Atualizar")
    print("4.	Excluir")
    print("0.   Retornar ao menu principal")

# Loop e seleçao das opções do menu principal

while True:
    mostrar_menu_principal()
    opc_menu_princ = int(input("Selecione a opção principal desejada: "))
    if opc_menu_princ == 0:
        print("Saindo do programa")
        break
    elif opc_menu_princ in [1, 2, 3, 4, 5]:
        if opc_menu_princ == 1: 
            print("[Estudantes] Menu de operações")
            mostrar_menu_operacoes()
        elif opc_menu_princ == 2:
            print("[Disciplinas] Menu de operações")
            mostrar_menu_operacoes()
        elif opc_menu_princ == 3:
            print("[Professores] Menu de operações")
            mostrar_menu_operacoes()
        elif opc_menu_princ == 4:
            print("[Turmas] Menu de operações")
            mostrar_menu_operacoes()
        elif opc_menu_princ == 5:
            print("[Matriculas] Menu de operações")

# Opçoes menu secundario

        opc_menu_secund = 1
        while opc_menu_secund != 0:
                estudantes = []
                opc_menu_secund = int(input("Selecione a opção secundario desejada: "))
                # Gerar dados dos ESTUDANTES juntamente com a opcao INCLUSAO
                if opc_menu_princ == 1 and opc_menu_secund == 1 :
                    print("    ÁREA DE INCLUSÃO     ")
                    print("        CADASTRO         ")
                    print("       ESTUDANTES       ")
                    nome_estudante = str(input("Digite o nome completo do aluno: "))
                    estudantes.append(nome_estudante)
                    print(estudantes)

                # Gerar listagem ESTUDANTES 
                elif opc_menu_princ == 1 and opc_menu_secund == 2 :
                    print(estudantes)
                    print('EM DESENVOLVIMENTO...')
                    continue
                elif opc_menu_secund == 3:
                    print("Atualizar")
                    print('EM DESENVOLVIMENTO...')
                elif opc_menu_secund == 4:
                    print('EM DESENVOLVIMENTO...')
                elif opc_menu_secund == 0:
                    print("Volta ao MENU PRINCIPAL")
                    print('Você voltou ao MENU PRINCIPAL')
                    break
                else:
                    print("Opção inválida!")