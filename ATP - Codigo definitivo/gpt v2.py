# Importar biblioteca tempo para delay
import time
import json

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

def salvar_arquivo(lista, arquivo):
    with open(arquivo, 'w') as arquivo_op:
        json.dump(lista, arquivo_op)

def ler_arquivo(arquivo):
    try:
        with open(arquivo, 'r') as arquivo_op:
            return json.load(arquivo_op)
    except FileNotFoundError:
        return []
    except:
        print("Erro ao ler o arquivo.")
        return []

def adicionar_dados(opcao_menu, lista, arquivo):
    while True:
        print("=" * 30)
        print(f"    ÁREA DE INCLUSÃO     ")
        print(f"        CADASTRO         ")
        print(f"       {opcao_menu.upper()}       ")
        print("=" * 30)
        
        # Aqui você pode adicionar lógica específica para cada opção do menu
        if opcao_menu == "estudantes":
            nome = input("Digite o nome completo: ")
            cpf = input("Digite o CPF: ")
            codigo = gerar_codigo(lista)
            novo_dado = {"Código": codigo, "Nome": nome, "CPF": cpf}
        elif opcao_menu == "disciplinas":
            # Lógica para adicionar disciplinas
        elif opcao_menu == "professores":
            # Lógica para adicionar professores
        elif opcao_menu == "turmas":
            # Lógica para adicionar turmas
        elif opcao_menu == "matrículas":
            # Lógica para adicionar matrículas
        
        lista.append(novo_dado)
        print(f"{opcao_menu.capitalize()} cadastrado com sucesso.")
        salvar_arquivo(lista, arquivo)
        continuar = input(f"Deseja adicionar outro {opcao_menu}? (S/N): ").strip().lower()
        if continuar != 's':
            break

# Função para gerar um novo código
def gerar_codigo(lista):
    proximo_codigo = max([0] + [item.get('Código', 0) for item in lista]) + 1
    return proximo_codigo

# Função listar dados genérica
def listar_dados(opcao_menu, lista):
    print("=" * 30)
    print(f"Listagem de {opcao_menu.capitalize()}:")
    if not lista:
        print(f"Não há {opcao_menu} cadastrados")
        time.sleep(1)
    else:
        for item in lista:
            print(", ".join([f"{key}: {value}" for key, value in item.items()]))
            print("-" * 20)
            time.sleep(1)

# Função editar dados genérica
def editar_dados(opcao_menu, lista, arquivo):
    codigo = int(input(f"Digite o código do {opcao_menu} que deseja editar: "))
    for item in lista:
        if item.get('Código') == codigo:
            print("Dados atuais do {opcao_menu}:")
            for key, value in item.items():
                print(f"{key}: {value}")
            print("-" * 20)
            
            # Aqui você pode adicionar lógica específica para cada opção do menu
            if opcao_menu == "estudantes":
                nome = input("Digite o novo nome: ")
                cpf = input("Digite o novo CPF: ")
                item["Nome"] = nome
                item["CPF"] = cpf
            
            print(f"{opcao_menu.capitalize()} editado com sucesso.")
            salvar_arquivo(lista, arquivo)
            break
    else:
        print(f"{opcao_menu.capitalize()} não encontrado.")

# Função excluir dados genérica
def excluir_dados(opcao_menu, lista, arquivo):
    codigo = int(input(f"Digite o código do {opcao_menu} que deseja excluir: "))
    for item in lista:
        if item.get('Código') == codigo:
            lista.remove(item)
            print(f"{opcao_menu.capitalize()} excluído com sucesso.")
            salvar_arquivo(lista, arquivo)
            break
    else:
        print(f"{opcao_menu.capitalize()} não encontrado.")

# Loop Menu principal
while True:
    mostrar_menu_principal()
    opc_menu_princ = int(input("Selecione a opção principal desejada: "))
    if opc_menu_princ == 0:
        print("Saindo do programa")
        break
    elif opc_menu_princ == 1:
        opcao_menu = "estudantes"
        lista = estudantes
        arquivo = "estudantes.json"
    elif opc_menu_princ == 2:
        opcao_menu = "disciplinas"
        lista = disciplinas
        arquivo = "disciplinas.json"
    elif opc_menu_princ == 3:
        opcao_menu = "professores"
        lista = professores
        arquivo = "professores.json"
    elif opc_menu_princ == 4:
        opcao_menu = "turmas"
        lista = turmas
        arquivo = "turmas.json"
    elif opc_menu_princ == 5:
        opcao_menu = "matrículas"
        lista = matriculas
        arquivo = "matriculas.json"
    else:
        print("Opção inválida no menu principal!")
        continue
    
    # Loop menu secundário, somente executará o código se a opc_menu_princ for válida
    opc_menu_secund = 1
    while opc_menu_secund != 0:
        mostrar_menu_operacoes(opcao_menu)
        opc_menu_secund = int(input(f"Selecione a opção secundária desejada para {opcao_menu}: "))
        if opc_menu_secund == 1:
            adicionar_dados(opcao_menu, lista, arquivo)
        elif opc_menu_secund == 2:
            listar_dados(opcao_menu, lista)
        elif opc_menu_secund == 3:
            editar_dados(opcao_menu, lista, arquivo)
        elif opc_menu_secund == 4:
            excluir_dados(opcao_menu, lista, arquivo)
        elif opc_menu_secund == 0:
            print("Retornando ao MENU")
