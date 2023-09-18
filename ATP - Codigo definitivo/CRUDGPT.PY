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

# Lista para guardar dados dos estudantes
estudantes = []

# Variável para gerar códigos de estudante
proximo_codigo = 1

# Função para gerar um novo código de estudante
def gerar_codigo():
    global proximo_codigo
    codigo = proximo_codigo
    proximo_codigo += 1
    return codigo

# Função adicionar estudante:
def adicionar_estudante():
    while True:
        print("=" * 30)
        print("    ÁREA DE INCLUSÃO     ")
        print("        CADASTRO         ")
        print("       ESTUDANTES       ")
        print("=" * 30)
        nome_estudante = input("Digite o nome completo do estudante: ")
        cpf_estudante = input("Digite o CPF do estudante: ")
        codigo_estudante = gerar_codigo()
        estudante = {"Código": codigo_estudante, "Nome": nome_estudante, "CPF": cpf_estudante}
        estudantes.append(estudante)
        print("Estudante cadastrado com sucesso.")
        continuar = input("Deseja adicionar outro estudante? (S/N): ").strip().lower()
        if continuar != 's':
            break

# Função listar estudantes:
def listar_estudantes():
    print("=" * 30)
    print("Listagem de Estudantes:")
    if not estudantes:
        print("Não há estudantes cadastrados")
        time.sleep(1)
    else:
        for estudante in estudantes:
            print(f"Código: {estudante['Código']} , Nome: {estudante['Nome']} , CPF: {estudante['CPF']}")
            print("-" * 20)
            time.sleep(1)

# Função editar estudante:
def editar_estudante():
    codigo = int(input("Digite o código do estudante que deseja editar: "))
    for estudante in estudantes:
        if estudante['Código'] == codigo:
            print("Dados atuais do estudante:")
            print(f"Código: {estudante['Código']}")
            print(f"Nome: {estudante['Nome']}")
            print(f"CPF: {estudante['CPF']}")
            print("-" * 20)
            nome_estudante = input("Digite o novo nome do estudante: ")
            cpf_estudante = input("Digite o novo CPF do estudante: ")
            estudante['Nome'] = nome_estudante
            estudante['CPF'] = cpf_estudante
            print("Estudante editado com sucesso.")
            break
    else:
        print("Estudante não encontrado.")

# Função excluir estudante:
def excluir_estudante():
    codigo = int(input("Digite o código do estudante que deseja excluir: "))
    for estudante in estudantes:
        if estudante['Código'] == codigo:
            estudantes.remove(estudante)
            print("Estudante excluído com sucesso.")
            break
    else:
        print("Estudante não encontrado.")

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
    
    # Loop menu secundário, somente executará o código se a opc_menu_princ for válida
    opc_menu_secund = 1
    while opc_menu_secund != 0:
        mostrar_menu_operacoes(opcao_menu)
        opc_menu_secund = int(input(f"Selecione a opção secundária desejada para {opcao_menu}: "))
        if opc_menu_secund == 1:
            adicionar_estudante()
        elif opc_menu_secund == 2:
            listar_estudantes()
        elif opc_menu_secund == 3:
            editar_estudante()
        elif opc_menu_secund == 4:
            excluir_estudante()
        elif opc_menu_secund == 0:
            print("Retornando ao MENU PRINCIPAL")
            break
        else:
            print("Opção inválida no menu secundário!")
