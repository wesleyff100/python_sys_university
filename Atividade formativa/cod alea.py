import time

list_std = {}
print("[     SEJA BEM-VINDO!     ]")
time.sleep(0.5)
print("[     SEJA BEM-VINDO!     ]")
time.sleep(0.5)
print("[     SEJA BEM-VINDO!     ]")
time.sleep(0.5)
print("-" * 27)
print("[     MENU PRINCIPAL      ]")
time.sleep(0.3)
print("-" * 27)
opcao = 1
while opcao != 0:
    print("""[1] - Estudantes""")
    print("""[2] - Dísciplinas""")
    print("""[3] - Professores""")
    print("""[4] - Turmas""")
    print("""[5] - Matrículas""")
    print("""[0] - Sair""")
    print("-" * 27)
    opcao = int(input("Digite uma opção: "))
    print("-" * 27)
    if opcao == 1:
        print('[   ÁREA DOS ESTUDANTES   ]')
    elif opcao == 2:
        print('[  ÁREA DAS DISCIPLINAS   ]')
    elif opcao == 3:
        print('[  ÁREA DOS PROFESSORES   ]')
    elif opcao == 4:
        print('[-------- TURMAS ---------]')
    elif opcao == 5:
        print('[------ MATRÍCULAS -------]')
    elif opcao == 0:
        print("[  OPERAÇÃO FINALIZADA!   ]")
        print("-" * 27)
        time.sleep(0.5)
        print("[   BOM ESTUDO!           ]")
        time.sleep(0.5)
        print("[       BOM ESTUDO!       ]")
        time.sleep(0.5)
        print("[           BOM ESTUDO!   ]")
        print("-" * 27)
        break
    else:
        print("OPÇÃO INVÁLIDA!")
    print('-' * 27)

    acao = 1
    while acao != 0:
        print("""[1] - Incluir""")
        print("""[2] - Listar""")
        print("""[3] - Atualizar""")
        print("""[4] - Excluir""")
        print("""[0] - Voltar ao MENU PRINCIPAL""")
        print("-" * 27)
        acao = int(input("Escolha uma opção: "))
        if acao == 1:
            alunos = {}
            print("[    ÁREA DE INCLUSÃO     ]")
            print("[        CADASTRO         ]")

            while True:
                nome1 = input('Digite o nome completo do aluno: ')
    

                nasc = input('Digite a data de Nascimento: ')
                if nome1 in alunos:
                    if input(f'Aluno cadastrado com data de nascimento {alunos[nome1]}, '
                             f'Deseja alterar? (sim/não)') == "não":
                        continue
                if nasc in alunos.values():
                    print('Dados cadastrado com sucesso!')
                    continue
                alunos[nome1] = nasc

                if input('Deseja cadastrar um novo aluno (sim/não): ') == 'não':
    
                    break

            print('Cadastro finalizado com sucesso!')

            print(alunos)
            list_std = alunos
        elif acao == 2:
            print("Lista")
            print('EM DESENVOLVIMENTO...')
            continue
        elif acao == 3:
            print("Atualizar")
            print('EM DESENVOLVIMENTO...')
        elif acao == 4:
            print('EM DESENVOLVIMENTO...')
        elif acao == 0:
            print("Volta ao MENU PRINCIPAL")
            print('Você voltou ao MENU PRINCIPAL')
        else:
            print("Opção inválida!")