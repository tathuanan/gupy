######################## OBSERVAÇÕES ########################
# Variáveis x e xx são variáveis de controle do loop while ##
#############################################################
from time import sleep
from datetime import date

VARIAVEIS = __import__('Main')
BONUS = __import__('Bonus')

def primeira_parte(opcao, animais = None, falas_do_cantor = None):

    ### Variáveis - INÍCIO ###
    erguei = 'Erguei as mãos'
    gloria = 'e dai glória a Deus'
    cantai = 'E cantai'
    subiram = 'Os animaizinhos subiram de dois em dois'
    arca = 'Deus disse a Noé: Contrói uma arca'
    feita_de_madeira = 'Que seja feita\nDe madeira'
    por_isso = 'Por isso...!'
    ### Variáveis - FIM ###

    ### Funções - INÍCIO ###
    def filhos(tipo):
        if tipo == 'como':
            return 'como os filhos do Senhor'
        else:
            return 'para os filhos do Senhor'
    ### Funções - FIM ###

    # Primeira Estrofe
    x=0
    while x < 2:
        print(f'{erguei} {gloria}')
        x += 1
    print(erguei)
    print(f'{cantai} {filhos("como")}\n')

    # Estrofes que contém os animais
    if opcao == 2:
            print(falas_do_cantor[1])
    for animal in animais:
        print(f'{subiram}\n{subiram}')
        print(f'{animal[0]}\n{animal[1]}, {filhos("como")}\n')

    # Estrofe da construção da arca
    x=0
    while x < 2:
        print(f'{arca}')
        x += 1
    print(f'{feita_de_madeira} {filhos("para")}\n')

    # Final da primeira parte
    print(por_isso)
    x=0
    while x < 3:
        xx = 0
        while xx < 2:
            print(f'{erguei} {gloria}')
            xx += 1
        print(erguei)
        if opcao == 2 and x == 1:
            print(f'{cantai} {filhos("como")} {falas_do_cantor[2]}\n')
        else:
            print(f'{cantai} {filhos("como")}\n')
        x += 1

def segunda_parte(opcao, falas_do_cantor = None, partes_do_corpo = None):

    ### Variáveis - INÍCIO ###

    lados_e_acoes = {
    'direito' : 'direito',
    'esquerdo' : 'esquerdo',
    'direita' : 'direita',
    'esquerda' : 'esquerda',
    'balanca' : 'Balança',
    'voltinha' : 'dá uma voltinha',
    'pulinho' : 'Dá um pulinho',
    'abraca' : 'e abraça o irmão',
}
    
    atencao = "E atenção agora, porque\n"

    estrofe_principal = [
        "O senhor tem muitos filhos",
        "Muitos filhos ele tem",
        "Eu sou um deles, você também",
        "Louvemos ao senhor",
    ]
        
    secundaria_um = (f'{partes_do_corpo[1].title()} {lados_e_acoes["direito"]}')
    secundaria_dois = (f'{secundaria_um}, {partes_do_corpo[1]} {lados_e_acoes["esquerdo"]}')
    secundaria_tres = (f'{secundaria_dois}\n{partes_do_corpo[2].title()} {lados_e_acoes["direita"]}')
    secundaria_quatro = (f'{secundaria_tres}, {partes_do_corpo[2]} {lados_e_acoes["esquerda"]}')
    secundaria_cinco = (f'{secundaria_quatro}\n{lados_e_acoes["balanca"]} {partes_do_corpo[3]}')
    secundaria_seis = (f'{secundaria_cinco}, {lados_e_acoes["voltinha"]}')
    secundaria_sete = (f'{secundaria_seis}\n{lados_e_acoes["pulinho"]}')
    secundaria_oito = (f'{secundaria_sete} {lados_e_acoes["abraca"]}')

    estrofes_secundarias = [
        secundaria_um,
        secundaria_dois,
        secundaria_tres,
        secundaria_quatro,
        secundaria_cinco,
        secundaria_seis,
        secundaria_sete,
        secundaria_oito
        ]
    ### Variáveis - FIM ###

    ### Funções - INÍCIO ###
    def montando_estrofe_principal(opcao):
        if opcao == 2:
            if x == 4:
                print(f'{estrofe_principal[0]} {falas_do_cantor[4]}')
            elif x == 7:
                print(f'{estrofe_principal[0]} {falas_do_cantor[7]}')
            else:
                print(estrofe_principal[0])
            if x == 2:
                print(f'{estrofe_principal[1]} {falas_do_cantor[3]}')
            elif x == 6:
                print(f'{estrofe_principal[1]} {falas_do_cantor[6]}')
            else:
                print(estrofe_principal[1])
            if x == 4:
                print(f'{estrofe_principal[2]} {falas_do_cantor[5]}')
            else:
                print(estrofe_principal[2])
            print(f'{estrofe_principal[3]}\n')
        else:       
            print(estrofe_principal[0])
            print(estrofe_principal[1])
            print(estrofe_principal[2])
            print(f'{estrofe_principal[3]}\n')
    ### Funções - FIM ###
    print(atencao)
    x=0
    while x < 8:
        montando_estrofe_principal(opcao)
        print(f'{estrofes_secundarias[x]}\n')
        x += 1

def musica_completa(opcao, animais = None, falas_do_cantor = None, partes_do_corpo = None):
    primeira_parte(opcao, animais, falas_do_cantor)
    segunda_parte(opcao, falas_do_cantor, partes_do_corpo)

def menu_reproduzir_musica():

    ### Variáveis - INÍCIO ###
    menu_principal = """
Por favor, Escolha uma opção:
1. Primeira parte da música
2. Segunda parte da música
3. Música completa
4. Encerrar
0. Bônus
"""

    menu_secundario_primeira_parte = """
Por favor, Escolha uma opção:
1. Reproduzir música sem as falas do cantor
2. Reproduzir música com as falas do cantor
3. Alterar alguma fala do cantor que é exibida na música antes de reproduzir
4. Alterar algum par de animais exibidos na música antes de reproduzir
5. Voltar ao menu anterior
"""

    menu_secundario_segunda_parte = """
Por favor, Escolha uma opção:
1. Reproduzir música sem as falas do cantor
2. Reproduzir música com as falas do cantor
3. Alterar alguma fala do cantor que é exibida na música antes de reproduzir
4. Alterar alguma parte do corpo que é exibida na música antes de reproduzir
5. Voltar ao menu anterior
"""

    menu_secundario_musica_completa = """
Por favor, Escolha uma opção:
1. Reproduzir música sem as falas do cantor
2. Reproduzir música com as falas do cantor
3. Alterar alguma fala do cantor que é exibida na música antes de reproduzir
4. Alterar algum par de animais exibidos na música antes de reproduzir
5. Alterar alguma parte do corpo que é exibida na música antes de reproduzir
6. Voltar ao menu anterior
"""
    copia_animais = VARIAVEIS.animais_originais.copy()
    copia_falas_do_cantor = VARIAVEIS.falas_do_cantor_originais.copy()
    copia_partes_do_corpo = VARIAVEIS.partes_do_corpo_originais.copy()
    ### Variáveis - FIM ###

    print(f"Olá hoje é {date.today().strftime('%d/%m/%Y')} e esse é o reprodutor automático da música 'Erguei As Mãos' do cantor Padre Marcelo Rossi!")

    while True:
        print(menu_principal)
        
        opcao = input()

        if opcao == "1":
            while True:
                print(menu_secundario_primeira_parte)
                opcao_secundaria = int(input())
                if opcao_secundaria in (1,2):
                    print("\nReproduzindo a primeira parte da música:\n")
                    primeira_parte(opcao_secundaria, falas_do_cantor = copia_falas_do_cantor, animais = copia_animais)
                    break
                elif opcao_secundaria == 3:
                    while True:
                        print("Por favor, escolha a fala do cantor que é exibida na música que deseja alterar:")
                        for falas in copia_falas_do_cantor.keys():
                            if falas > 2:
                                break
                            print(f'{falas}. {copia_falas_do_cantor[falas]}')
                        print("0. Retornar ao menu anterior")
                        escolha = int(input())
                        if escolha == 0:
                            break
                        elif escolha in (1,2):
                            nova_fala = input("Digite a nova fala do cantor que será exibida: ")
                            copia_falas_do_cantor[escolha] = nova_fala
                            break
                        else:
                            print("\nOpção inválida. Tente novamente.\n")
                elif opcao_secundaria == 4:
                    while True:
                        print("Por favor, escolha o par de animais que são exibidos na música que deseja alterar:")
                        numero = 1 #Variável de controle
                        for animais in VARIAVEIS.animais_originais:
                            print(f'{numero}. {animais}')
                            numero += 1
                        print("0. Retornar ao menu anterior")
                        escolha = int(input())
                        escolha -= 1
                        if escolha == -1:
                            break
                        elif escolha <= (len(VARIAVEIS.animais_originais)):
                            novo_animal_um = input("Digite o primeiro novo animal: ")
                            novo_animal_dois = input("Digite o segundo novo animal: ")
                            copia_animais[escolha][0] = novo_animal_um
                            copia_animais[escolha][1] = novo_animal_dois
                            break
                        else:
                            print("\nOpção inválida. Tente novamente.\n")
                elif opcao_secundaria == 5:
                    break
                else:
                    print("\nOpção inválida. Tente novamente.")
        elif opcao == "2":
            while True:
                print(menu_secundario_segunda_parte)
                opcao_secundaria = int(input())
                if opcao_secundaria in (1,2):
                    print("\nReproduzindo a segunda parte da música:\n")
                    segunda_parte(opcao_secundaria, falas_do_cantor = copia_falas_do_cantor, partes_do_corpo = copia_partes_do_corpo)
                    break
                elif opcao_secundaria == 3:
                    while True:
                        print("Por favor, escolha a fala do cantor que é exibida na música que deseja alterar:")
                        for falas in copia_falas_do_cantor.keys():
                            if falas > 2:
                                print(f'{falas-2}. {copia_falas_do_cantor[falas]}')
                        print("0. Retornar ao menu anterior")
                        escolha = int(input())
                        escolha += 2
                        if escolha == 2:
                            break
                        elif escolha in range(3, len(copia_falas_do_cantor)+1):
                            nova_fala = input("Digite a nova fala do cantor que será exibida: ")
                            copia_falas_do_cantor[escolha] = nova_fala
                            break
                        else:
                            print("\nOpção inválida. Tente novamente.\n")
                elif opcao_secundaria == 4:
                    while True:
                        print("Por favor, escolha a parte do corpo que é exibida na música que deseja alterar:")
                        for partes in copia_partes_do_corpo.keys():
                            print(f'{partes}. {copia_partes_do_corpo[partes]}')
                        print("0. Retornar ao menu anterior")
                        escolha = int(input())
                        if escolha == 0:
                            break
                        elif escolha in range(1, len(copia_partes_do_corpo)+1):
                            nova_parte = input("Digite a nova parte do corpo que será exibida na música: ")
                            copia_partes_do_corpo[escolha] = nova_parte
                            break
                        else:
                            print("\nOpção inválida. Tente novamente.\n")
                elif opcao_secundaria == 5:
                    break
                else:
                    print("\nOpção inválida. Tente novamente.")
        elif opcao == "3":
            while True:
                print(menu_secundario_musica_completa)
                opcao_secundaria = int(input())
                if opcao_secundaria in (1,2):
                    print("\nReproduzindo a música completa:\n")
                    musica_completa(opcao_secundaria, animais = copia_animais, falas_do_cantor = copia_falas_do_cantor, partes_do_corpo = copia_partes_do_corpo)
                    break
                elif opcao_secundaria == 3:
                    while True:
                        print("Por favor, escolha a fala do cantor que é exibida na música que deseja alterar:")
                        for falas in copia_falas_do_cantor.keys():
                            print(f'{falas}. {copia_falas_do_cantor[falas]}')
                        print("0. Retornar ao menu anterior")
                        escolha = int(input())
                        if escolha == 0:
                            break
                        elif escolha in range(1, len(copia_falas_do_cantor)+1):
                            nova_fala = input("Digite a nova fala do cantor que será exibida: ")
                            copia_falas_do_cantor[escolha] = nova_fala
                            break
                        else:
                            print("\nOpção inválida. Tente novamente.\n")
                elif opcao_secundaria == 4:
                    while True:
                        print("Por favor, escolha o par de animais que são exibidos na música que deseja alterar:")
                        numero = 1 #Variável de controle
                        for animais in VARIAVEIS.animais_originais:
                            print(f'{numero}. {animais}')
                            numero += 1
                        print("0. Retornar ao menu anterior")
                        escolha = int(input())
                        escolha -= 1
                        if escolha == -1:
                            break
                        elif escolha <= (len(VARIAVEIS.animais_originais)):
                            novo_animal_um = input("Digite o primeiro novo animal: ")
                            novo_animal_dois = input("Digite o segundo novo animal: ")
                            copia_animais[escolha][0] = novo_animal_um
                            copia_animais[escolha][1] = novo_animal_dois
                            break
                        else:
                            print("\nOpção inválida. Tente novamente.\n")
                elif opcao_secundaria == 5:
                    while True:
                        print("Por favor, escolha a parte do corpo que é exibida na música que deseja alterar:")
                        for partes in copia_partes_do_corpo.keys():
                            print(f'{partes}. {copia_partes_do_corpo[partes]}')
                        print("0. Retornar ao menu anterior")
                        escolha = int(input())
                        if escolha == 0:
                            break
                        elif escolha in range(1, len(copia_partes_do_corpo)+1):
                            nova_parte = input("Digite a nova parte do corpo que será exibida na música: ")
                            copia_falas_do_cantor[escolha] = nova_parte
                            break
                        else:
                            print("\nOpção inválida. Tente novamente.\n")
                elif opcao_secundaria == 6:
                    break
                else:
                    print("\nOpção inválida. Tente novamente.")
        elif opcao == "4":
            print("\nEncerrando o programa")
            break
        elif opcao == "0":
            BONUS.imprimir_musica_por_palavra(BONUS.musica)
        else:
            print("Opção inválida. Tente novamente.")

        ### Voltando os valores originais das listas e dicionários ###
        copia_animais = VARIAVEIS.animais_originais.copy()
        copia_falas_do_cantor = VARIAVEIS.falas_do_cantor_originais.copy()
        copia_partes_do_corpo = VARIAVEIS.partes_do_corpo_originais.copy()
        ##################################################################