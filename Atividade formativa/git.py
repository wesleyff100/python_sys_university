import json
import time
import os

# Define um diretório para armazenar os arquivos JSON
DATA_DIR = "data"

# Funcao para interromper programa
def finalizar_programa():
    print('Finalizando o programa....')
    exit(0)
# Funcao espera execução
def espera():
    input('\nPressione [ENTER] para continuar')

def menu_principal():
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
    arquivo_path = os.path.join(DATA_DIR, arquivo)
    try:
        with open(arquivo_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_dados(arquivo, dados):
    arquivo_path = os.path.join(DATA_DIR, arquivo)
    with open(arquivo_path, 'w') as f:
        json.dump(dados, f)

    print("Dados salvos com sucesso!")
    espera()

def validar_codigo(arquivo, codigo):
    dados = carregar_dados(arquivo)
    return codigo in dados

def criar_registro(arquivo, campos, validacoes=None):
    dados = carregar_dados(arquivo)
    registro = {}

    for campo in campos:
        valor = input(f'Insira o {campo}: ')

        if validacoes and campo in validacoes:
            arquivo_validacao, mensagem_erro = validacoes[campo]
            while not validar_codigo(arquivo_validacao, valor):
                print(mensagem_erro)
                valor = input(f'Insira o {campo} novamente: ')

        registro[campo] = valor

    codigo = registro[campos[0]]
    dados[codigo] = registro
    salvar_dados(arquivo, dados)

def listar_registros(arquivo, opcao_menu):
    dados = carregar_dados(arquivo)
    
    if not dados:
        print(f"Não há dados de {opcao_menu.lower()} cadastrados.")
    else:
        for codigo, registro in dados.items():
            print(f'{opcao_menu} {codigo}: {registro}')

    espera()

def alterar_registro(arquivo, campos, validacoes=None):
    dados = carregar_dados(arquivo)
    codigo = input(f'Insira o {campos[0]} do registro que deseja alterar: ')

    if codigo not in dados:
        print(f'Registro com {campos[0]} {codigo} não encontrado!')
        espera()
    else:
        registro_alterado = {}

        for campo in campos:
            novo_valor = input(f'Insira o novo {campo}: ')

            if validacoes and campo in validacoes:
                arquivo_validacao, mensagem_erro = validacoes[campo]
                while not validar_codigo(arquivo_validacao, novo_valor):
                    print(mensagem_erro)
                    novo_valor = input(f'Insira o novo {campo} novamente: ')

            registro_alterado[campo] = novo_valor

        if registro_alterado[campos[0]] != codigo:
            dados.pop(codigo)
            dados[registro_alterado[campos[0]]] = registro_alterado
        else:
            dados[codigo] = registro_alterado

        salvar_dados(arquivo, dados)

def excluir_registro(arquivo, campo_codigo):
    dados = carregar_dados(arquivo)
    codigo = input(f'Insira o {campo_codigo} do registro que deseja excluir: ')

    if codigo not in dados:
        print(f'Registro com {campo_codigo} {codigo} não encontrado!')
        espera()
    else:
        del dados[codigo]
        salvar_dados(arquivo, dados)

def main():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    arquivos = {
        1: ('estudantes.json', 'ESTUDANTES', ['Código do estudante', 'Nome do estudante', 'CPF do estudante']),
        2: ('professores.json', 'PROFESSORES', ['Código do professor', 'Nome do professor', 'CPF do professor']),
        3: ('disciplinas.json', 'DISCIPLINAS', ['Código da disciplina', 'Nome da disciplina']),
        4: ('turmas.json', 'TURMAS', ['Código da turma', 'Código do professor', 'Código da disciplina']),
        5: ('matriculas.json', 'MATRÍCULAS', ['Código da matrícula', 'Código da turma', 'Código do estudante'])
    }

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

if __name__ == "__main__":
    main()
