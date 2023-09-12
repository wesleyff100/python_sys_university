# Definir os menus
def mostrar_menu_principal():
    print("-" * 20)
    print("Bem-vindo ao menu principal")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

def mostrar_menu_operacoes(opcao_menu):
    print(f"1. Incluir {opcao_menu}")
    print(f"2. Listar {opcao_menu}")
    print(f"3. Atualizar {opcao_menu}")
    print(f"4. Excluir {opcao_menu}")
    print("0. Retornar ao menu principal")

# Listas para armazenar dados
estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

# Função para adicionar elementos
def adicionar_elemento(lista, tipo_elemento):
    while True:
        print(f"    ÁREA DE INCLUSÃO     ")
        print(f"        CADASTRO         ")
        print(f"       {tipo_elemento}       ")
        nome_elemento = input(f"Digite o nome completo do {tipo_elemento}: ")
        lista.append(nome_elemento)
        print(f"{tipo_elemento} cadastrado com sucesso.")
        continuar = input(f"Deseja adicionar outro {tipo_elemento}? (S/N): ").strip().lower()
        if continuar != 's':
            break

# Loop e seleção das opções do menu principal
while True:
    mostrar_menu_principal()
    opc_menu_princ = int(input("Selecione a opção principal desejada: "))
    if opc_menu_princ == 0:
        print("Saindo do programa")
        break
    elif opc_menu_princ in [1, 2, 3, 4, 5]:
        if opc_menu_princ == 1:
            opcao_menu = "estudantes"
            lista = estudantes
        elif opc_menu_princ == 2:
            opcao_menu = "disciplinas"
            lista = disciplinas
        elif opc_menu_princ == 3:
            opcao_menu = "professores"
            lista = professores
        elif opc_menu_princ == 4:
            opcao_menu = "turmas"
            lista = turmas
        elif opc_menu_princ == 5:
            opcao_menu = "matrículas"
            lista = matriculas

        # Opções do menu secundário
        opc_menu_secund = 1
        while opc_menu_secund != 0:
            mostrar_menu_operacoes(opcao_menu)
            opc_menu_secund = int(input(f"Selecione a opção secundária desejada para {opcao_menu}: "))
            if opc_menu_secund == 1:
                adicionar_elemento(lista, opcao_menu)
            elif opc_menu_secund == 2:
                print(f"Listagem de {opcao_menu}:")
                for elemento in lista:
                    print(elemento)
                    print("-" * 20)
            elif opc_menu_secund == 3:
                print(f'Atualizar {opcao_menu} - EM DESENVOLVIMENTO...')
            elif opc_menu_secund == 4:
                print(f'Excluir {opcao_menu} - EM DESENVOLVIMENTO...')
            elif opc_menu_secund == 0:
                print("Retornando ao MENU PRINCIPAL")
                break
            else:
                print("Opção inválida no menu secundário!")
    else:
        print("Opção inválida no menu principal!")
