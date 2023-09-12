# Aluno Wesley Cordeiro / Projeto Raciocionio organizacional

# Importar biblioteca tempo para delay

import time

# Definir os menus
def mostrar_menu_principal():
    print("=" * 30)
    print("Bem-vindo ao menu principal")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")
    print("=" * 30)


def mostrar_menu_operacoes(opcao_menu):
    print("=" * 30)
    print(f" MENU {opcao_menu.capitalize()}")
    print(f"1. Incluir {opcao_menu}")
    print(f"2. Listar {opcao_menu}")
    print(f"3. Atualizar {opcao_menu}")
    print(f"4. Excluir {opcao_menu}")
    print("0. Retornar ao menu principal")
    print("=" * 30)

# Lista para guardar dados
estudantes = []
# Função adicionar aluno:
def adicionar_aluno():
    while True:
        print("=" * 30 )
        print("    ÁREA DE INCLUSÃO     ")
        print("        CADASTRO         ")
        print("       ESTUDANTES       ")
        print("=" * 30 )
        nome_estudante = input("Digite o nome completo do aluno: ")
        estudantes.append(nome_estudante)
        print("Aluno cadastrado com sucesso.")
        continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().lower()
        if continuar != 's':
            break

# Loop Menu principal
while True:
    mostrar_menu_principal()
    opc_menu_princ = int(input("Selecione a opção principal desejada: "))
    if opc_menu_princ == 0:
        print("Saindo do programa")
        break
    elif opc_menu_princ == 1:
        opcao_menu = "estudantes"
    elif opc_menu_princ == 2:
        print("===== EM DESENVOLVIMENTO =====")
        time.sleep(1)
        continue
    elif opc_menu_princ == 3:
        print("===== EM DESENVOLVIMENTO =====")
        time.sleep(1)
        continue
    elif opc_menu_princ == 4:
        print("===== EM DESENVOLVIMENTO =====")
        time.sleep(1)
        continue
    elif opc_menu_princ == 5:
        print("===== EM DESENVOLVIMENTO =====")
        time.sleep(1)
        continue
    else:
        print("Opção inválida no menu principal!")
        continue
    
    #Loop menu secundario, somente executará o codigo se a opc_menu_princ for valida
    opc_menu_secund = 1
    while opc_menu_secund != 0:
        mostrar_menu_operacoes(opcao_menu)
        opc_menu_secund = int(input(f"Selecione a opção secundária desejada para {opcao_menu}: "))
        if opc_menu_secund == 1:
            adicionar_aluno()
        elif opc_menu_secund == 2:
            print(f"Listagem de {opcao_menu}:")
            if not estudantes:
                print("Não há estudantes cadastrados")
                time.sleep(1)
            else:
                for aluno in estudantes:
                    print(aluno)
                    print("-" * 20)
                    time.sleep(1)
        elif opc_menu_secund == 3:
            print('EM DESENVOLVIMENTO...')
        elif opc_menu_secund == 4:
            print('EM DESENVOLVIMENTO...')
        elif opc_menu_secund == 0:
            print("Retornando ao MENU PRINCIPAL")
            break
        else:
            print("Opção inválida no menu secundário!")
