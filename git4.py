import json
import time
import os

# Diretório onde será armazenado os arquivos JSON
DATA_DIR = "data"  

def finalizar_programa():
    # Função para finalizar o programa
    print('Finalizando o programa....')
    exit(0)

def espera():
    # Função para pausar a execução do programa até que o usuário pressione a tecla ENTER
    input('\nPressione [ENTER] para continuar')

def menu_principal():
    # Função que exibe o menu principal e recebe a opção escolhida pelo usuário
    print("=" * 30)
    print("Bem-vindo ao menu principal")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")
    print("=" * 30)
    return int(input("Escolha uma opção: "))

def menu_operacoes(opcao_menu):
    # Função que exibe o menu de operações e recebe a opção escolhida pelo usuário
    print("=" * 30)
    print(f"= MENU DE OPERAÇÕES [{opcao_menu}] =")
    time.sleep(0.5)
    print(f"1. Incluir {opcao_menu.lower()}")
    print(f"2. Listar {opcao_menu.lower()}")
    print(f"3. Atualizar {opcao_menu.lower()}")
    print(f"4. Excluir {opcao_menu.lower()}")
    print("0. Retornar ao menu principal")
    print("=" * 30)
    return int(input("Escolha uma opção: "))

def carregar_dados(arquivo):
    # Função para carregar as informações de um arquivo JSON. Caso o arquivo não exista, retorna um dicionário vazio.
    arquivo_path = os.path.join(DATA_DIR, arquivo)
    try:
        with open(arquivo_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    # função para salvar informações em um arquivo JSON
    arquivo_path = os.path.join(DATA_DIR, arquivo)
    with open(arquivo_path, 'w') as f:
        json.dump(dados, f)
    print("Dados salvos com sucesso!")
    espera()

def validar_codigo(arquivo, codigo):
    # Função para validar se um código já existe em um arquivo JSON específico
    dados = carregar_dados(arquivo)
    return codigo in dados

def criar_registro(arquivo, campos, validacoes=None):
    # Função para criar e salvar um novo registro em um arquivo JSON específico
    dados = carregar_dados(arquivo) # Carrega os dados existentes do arquivo
    registro = {} # Cria um dicionário vazio para armazenar o novo registro

    for campo in campos:
        valor = input(f'Insira o {campo}: ')

        if validacoes and campo in validacoes: # Verifica se existem validações para o campo atual e aplica-as, se houver
            arquivo_validacao, mensagem_erro = validacoes[campo]
            while not validar_codigo(arquivo_validacao, valor):
                print(mensagem_erro)
                valor = input(f'Insira o {campo} novamente: ')

        registro[campo] = valor # Armazena o valor do campo no registro

    codigo = registro[campos[0]] # Obtém o código do registro
    dados[codigo] = registro # Adiciona o registro aos dados existentes
    salvar_dados(arquivo, dados) # Salva os dados atualizados no arquivo

def listar_registros(arquivo, opcao_menu):
    # Função para listar todos os registros de um arquivo JSON específico
    dados = carregar_dados(arquivo)
    
    if not dados:
        print(f"Não há dados de {opcao_menu.lower()} cadastrados.")
    else:
        for codigo, registro in dados.items():
            print(f'{opcao_menu} {codigo}: {registro}')

    espera()

def alterar_registro(arquivo, campos, validacoes=None):
    # Função para alterar um registro existente em um arquivo JSON específico
    dados = carregar_dados(arquivo) # Carrega os dados do arquivo
    codigo = input(f'Insira o {campos[0]} do registro que deseja alterar: ')

    if codigo not in dados: # Verifica se o registro com o código especificado existe
        print(f'Registro com {campos[0]} {codigo} não encontrado!')
        espera()
    else:
        registro_alterado = {}

        for campo in campos:
            novo_valor = input(f'Insira o novo {campo}: ')

            if validacoes and campo in validacoes: # Realiza validações caso existam para o campo atual
                arquivo_validacao, mensagem_erro = validacoes[campo]
                while not validar_codigo(arquivo_validacao, novo_valor): # Realiza validações caso existam para o campo atual
                    print(mensagem_erro)
                    novo_valor = input(f'Insira o novo {campo} novamente: ')

            registro_alterado[campo] = novo_valor

        if registro_alterado[campos[0]] != codigo: # Verifica se o novo valor para o campo identificador do registro é diferente do valor original , Remove o registro original dos dados e adiciona o registro alterado com a nova chave
            dados.pop(codigo)
            dados[registro_alterado[campos[0]]] = registro_alterado
        else:
            dados[codigo] = registro_alterado # Substitui o registro original pelos dados do registro alterado

        salvar_dados(arquivo, dados)

def excluir_registro(arquivo, campo_codigo):
    # Função para excluir um registro de um arquivo JSON específico
    dados = carregar_dados(arquivo)
    codigo = input(f'Insira o {campo_codigo} do registro que deseja excluir: ')

    if codigo not in dados:
        print(f'Registro com {campo_codigo} {codigo} não encontrado!')
        espera()
    else:
        del dados[codigo]
        salvar_dados(arquivo, dados)

def main():
    # Função principal que executa o programa. Apresenta o menu principal ao usuário e executa as operações escolhidas pelo usuário a partir dos menus.
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
# Dicionário que mapeia cada opção ao seu respectivo nome de arquivo, nome do menu e campos.
    arquivos = {
        1: ('estudantes.json', 'ESTUDANTES', ['Código do estudante', 'Nome do estudante', 'CPF do estudante']),
        2: ('professores.json', 'PROFESSORES', ['Código do professor', 'Nome do professor', 'CPF do professor']),
        3: ('disciplinas.json', 'DISCIPLINAS', ['Código da disciplina', 'Nome da disciplina']),
        4: ('turmas.json', 'TURMAS', ['Código da turma', 'Código do professor', 'Código da disciplina']),
        5: ('matriculas.json', 'MATRÍCULAS', ['Código da matrícula', 'Código da turma', 'Código do estudante'])
    }
# Dicionário que contém validações para campos específicos em determinadas operações.
    validacoes = {
        4: {
            'Código do professor': ('professores.json', 'Professor não encontrado!'),
            'Código da disciplina': ('disciplinas.json', 'Disciplina não encontrada!')
        },
        5: {
            'Código da turma': ('turmas.json', 'Turma não encontrada!'),
            'Código do estudante': ('estudantes.json', 'Estudante não encontrado!')
        }
    }

    while True:
        opcao_principal = menu_principal()

        if opcao_principal == 0:
            finalizar_programa()

        if opcao_principal not in arquivos:
            print('Opção inválida!')
            espera()
            continue

        arquivo, opcao_menu, campos = arquivos[opcao_principal]
        validacoes_campos = validacoes.get(opcao_principal)

        while True:
            opcao_operacao = menu_operacoes(opcao_menu)

            if opcao_operacao == 0:
                break
            elif opcao_operacao == 1:
                criar_registro(arquivo, campos, validacoes_campos)
            elif opcao_operacao == 2:
                listar_registros(arquivo, opcao_menu)
            elif opcao_operacao == 3:
                alterar_registro(arquivo, campos, validacoes_campos)
            elif opcao_operacao == 4:
                excluir_registro(arquivo, campos[0])
            else:
                print('Opção inválida!')
                espera()

if __name__ == "__main__": # Validação para se certificar da execução do programa como script principal
    main()
