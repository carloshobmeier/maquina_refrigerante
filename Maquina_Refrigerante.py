# VARIÁVEIS
senha = 0
estoque_refrigerante = 2
quantidade_notas_200 = 12
quantidade_notas_100 = 22
quantidade_notas_50 = 35
quantidade_notas_20 = 65
quantidade_notas_10 = 105
quantidade_notas_5 = 165
quantidade_notas_2 = 165
quantidade_moedas_1real = 165
quantidade_moedas_50 = 165
quantidade_moedas_25 = 165
quantidade_moedas_10 = 800
quantidade_moedas_5 = 400
quantidade_moedas_1centavo = 500
saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)
preco_refrigerante = 4
valor_total_inserido = 0
valor_inserido = 0
nivel_acesso = 0
ciclo = 0

while ciclo == 0:


    # escolha de nível de acesso (administrador/consumidor)
    nivel_acesso = int(input("Olá. Digite 1 para acessar a máquina como administrador, e 2 para acessar como consumidor: "))
    while nivel_acesso != 1 and nivel_acesso != 2:
        nivel_acesso = int(input("Valor inválido. Digite 1 para acessar a máquina como administrador, e 2 para acessar como consumidor: "))


    # PARTE DO ADMINISTRADOR:

    if nivel_acesso == 1:

        # senha (evita que um consumidor possa simplesmente escolher acessar como administrador levar embora todo o dinheiro da máquina)
        print("-------------------------------------------------------------")
        print("Digite a sua senha para ter acesso ao nível de administrador!")
        print("-------------------------------------------------------------")
        senha = int(input("Qual é a sua senha? "))
        print("-------------------------------------------------------------")
        while senha != 12345678 and nivel_acesso == 1:
            nova_tentativa = int(input("Senha errada, deseja tentar novamente? (1 para sim e 2 para não): "))
            while nova_tentativa == 1 and senha != 12345678:
                senha = int(input("Qual é a sua senha? "))
                print("---------------------------------")
                if senha != 12345678:
                    nova_tentativa = int(input("Senha errada, deseja tentar novamente? (1 para sim e 2 para não): "))
            while nova_tentativa == 2:
                print("---------------------------------------------------")
                print("Você decidiu encerrar o programa. Tenha um bom dia.")
                print("---------------------------------------------------")
                nova_tentativa = 1
                nivel_acesso = 3

    if nivel_acesso == 1:
    # Menu princial do administrador:
        print("Bem vindo ao sistema, administrador!")
        print("------------------------------------")
        print("Digite 1 para inserir cédulas/moedas.")
        print("Digite 2 para retirar cédulas/moedas.")
        print("Digite 3 para inserir itens.")
        print("Digite 4 para retirar itens.")
        print("Digite 5 para visualizar o saldo de dinheiro e estoque da máquina.")
        print("Digite 6 para visualizar a quantidade de dinheiro por cédulas/moedas.")
        print("Digite outro valor para finalizar.")
        print("---------------------------------------------------------------------")
        opcao_menu = int(input("Qual operação você deseja realizar? "))
        print("---------------------------------------------------------------------")

        if opcao_menu == 1:  # Serve para inserir cédulas/moedas
            print("----------------------------------------------")
            print("Você poderá inserir 1 tipo de cédulas por vez.")
            print("Qual tipo de cédulas deseja inserir primeiro?")
            print("Digite 1 para inserir cédulas de R$200")
            print("Digite 2 para inserir cédulas de R$100")
            print("Digite 3 para inserir cédulas de R$50")
            print("Digite 4 para inserir cédulas de R$20")
            print("Digite 5 para inserir cédulas de R$10")
            print("Digite 6 para inserir cédulas de R$5")
            print("Digite 7 para inserir cédulas de R$2")
            print("Digite 8 para inserir moedas de R$1")
            print("Digite 9 para inserir moedas de R$0.50")
            print("Digite 10 para inserir moedas de R$0.25")
            print("Digite 11 para inserir moedas de R$0.10")
            print("Digite 12 para inserir moedas de R$0.05")
            print("Digite 13 para inserir moedas de R$0.01")
            print("----------------------------------------------")
            escolha_adicionar_mais_dinheiro = 1
            while escolha_adicionar_mais_dinheiro == 1:
                adicionar_dinheiro = float(input("Qual cédula/moeda você deseja inserir? "))
                quantidade_dinheiro = int(input("Quantas cédulas/moedas você deseja adicionar? "))
                if adicionar_dinheiro == 1:
                    quantidade_notas_200 = quantidade_notas_200 + quantidade_dinheiro
                elif adicionar_dinheiro == 2:
                    quantidade_notas_100 = quantidade_notas_100 + quantidade_dinheiro
                elif adicionar_dinheiro == 3:
                    quantidade_notas_50 = quantidade_notas_50 + quantidade_dinheiro
                elif adicionar_dinheiro == 4:
                    quantidade_notas_20 = quantidade_notas_20 + quantidade_dinheiro
                elif adicionar_dinheiro == 5:
                    quantidade_notas_10 = quantidade_notas_10 + quantidade_dinheiro
                elif adicionar_dinheiro == 6:
                    quantidade_notas_5 = quantidade_notas_5 + quantidade_dinheiro
                elif adicionar_dinheiro == 7:
                    quantidade_notas_2 = quantidade_notas_2 + quantidade_dinheiro
                elif adicionar_dinheiro == 8:
                    quantidade_moedas_1real = quantidade_moedas_1real + quantidade_dinheiro
                elif adicionar_dinheiro == 9:
                    quantidade_moedas_50 = quantidade_moedas_50 + quantidade_dinheiro
                elif adicionar_dinheiro == 10:
                    quantidade_moedas_25 = quantidade_moedas_25 + quantidade_dinheiro
                elif adicionar_dinheiro == 11:
                    quantidade_moedas_10 = quantidade_moedas_10 + quantidade_dinheiro
                elif adicionar_dinheiro == 12:
                    quantidade_notas_5 = quantidade_moedas_5 + quantidade_dinheiro
                elif adicionar_dinheiro == 13:
                    quantidade_moedas_1centavo = quantidade_moedas_1centavo + quantidade_dinheiro
                saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)
                escolha_adicionar_mais_dinheiro = int(input("Deseja adicionar mais dinheiro? Digite 1 para sim e 2 para não: "))
            print("---------------------------------------------------------------------")
            print("Quantidade final de notas de 200 reais", quantidade_notas_200)
            print("Quantidade final de notas de 100 reais", quantidade_notas_100)
            print("Quantidade final de notas de 50 reais", quantidade_notas_50)
            print("Quantidade final de notas de 20 reais", quantidade_notas_20)
            print("Quantidade final de notas de 10 reais", quantidade_notas_10)
            print("Quantidade final de notas de 5 reais", quantidade_notas_5)
            print("Quantidade final de notas de 2 reais", quantidade_notas_2)
            print("Quantidade final de moedas de 1 real", quantidade_moedas_1real)
            print("Quantidade final de moedas de 50 centavos", quantidade_moedas_50)
            print("Quantidade final de moedas de 25 centavos", quantidade_moedas_25)
            print("Quantidade final de moedas de 10 centavos", quantidade_moedas_10)
            print("Quantidade final de moedas de 5 centavos", quantidade_moedas_5)
            print("Quantidade final de moedas de 1 centavo", quantidade_moedas_1centavo)

        elif opcao_menu == 2:  # serve para fazer o saque de dinheiro
            print("----------------------------------------------")
            print("Você poderá retirar 1 tipo de cédulas por vez.")
            print("Qual tipo de cédulas deseja retirar primeiro?")
            print("----------------------------------------------")
            print("Digite 1 para retirar cédulas de R$200")
            print("Digite 2 para retirar cédulas de R$100")
            print("Digite 3 para retirar cédulas de R$50")
            print("Digite 4 para retirar cédulas de R$20")
            print("Digite 5 para retirar cédulas de R$10")
            print("Digite 6 para retirar cédulas de R$5")
            print("Digite 7 para retirar cédulas de R$2")
            print("Digite 8 para retirar moedas de R$1")
            print("Digite 9 para retirar moedas de R$0.50")
            print("Digite 10 para retirar moedas de R$0.25")
            print("Digite 11 para retirar moedas de R$0.10")
            print("Digite 12 para retirar moedas de R$0.05")
            print("Digite 13 para retirar moedas de R$0.01")
            print("----------------------------------------------")
            escolha_retirar_mais_dinheiro = 1
            while escolha_retirar_mais_dinheiro == 1:
                retirar_dinheiro = float(input("Qual cédula/moeda você deseja retirar? "))
                while retirar_dinheiro != 1 and retirar_dinheiro != 2 and retirar_dinheiro != 3 and retirar_dinheiro != 4 and retirar_dinheiro != 5 and retirar_dinheiro != 6 and retirar_dinheiro != 7 and retirar_dinheiro != 8 and retirar_dinheiro != 9 and retirar_dinheiro != 10 and retirar_dinheiro != 11 and retirar_dinheiro != 12 and retirar_dinheiro != 13:
                    retirar_dinheiro = float(input("Valor inválido, qual cédula/moeda você deseja retirar? "))
                if retirar_dinheiro == 1:
                    print("Você escolheu a nota de R$200")
                    print("Há um limite de", quantidade_notas_200, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_notas_200:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_notas_200 = quantidade_notas_200 - quantidade_saque
                elif retirar_dinheiro == 2:
                    print("Você escolheu a nota de R$100")
                    print("Há um limite de", quantidade_notas_100, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_notas_100:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_notas_100 = quantidade_notas_100 - quantidade_saque
                elif retirar_dinheiro == 3:
                    print("Você escolheu a nota de R$50")
                    print("Há um limite de", quantidade_notas_50, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_notas_50:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_notas_50 = quantidade_notas_50 - quantidade_saque    
                elif retirar_dinheiro == 4:
                    print("Você escolheu a nota de R$20")
                    print("Há um limite de", quantidade_notas_20, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_notas_20:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_notas_20 = quantidade_notas_20 - quantidade_saque
                elif retirar_dinheiro == 5:
                    print("Você escolheu a nota de R$10")
                    print("Há um limite de", quantidade_notas_10, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_notas_10:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_notas_10 = quantidade_notas_10 - quantidade_saque
                elif retirar_dinheiro == 6:
                    print("Você escolheu a nota de R$5")
                    print("Há um limite de", quantidade_notas_5, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_notas_5:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_notas_5 = quantidade_notas_5 - quantidade_saque
                elif retirar_dinheiro == 7:
                    print("Você escolheu a nota de R$2")
                    print("Há um limite de", quantidade_notas_2, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_notas_2:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_notas_2 = quantidade_notas_2 - quantidade_saque
                elif retirar_dinheiro == 8:
                    print("Você escolheu a moeda de R$1")
                    print("Há um limite de", quantidade_moedas_1real, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_moedas_1real:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_moedas_1real = quantidade_moedas_1real - quantidade_saque
                elif retirar_dinheiro == 9:
                    print("Você escolheu a moeda de R$0.50")
                    print("Há um limite de", quantidade_moedas_50, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_moedas_50:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_moedas_50 = quantidade_moedas_50 - quantidade_saque
                elif retirar_dinheiro == 10:
                    print("Você escolheu a moeda de R$0.25")
                    print("Há um limite de", quantidade_moedas_25, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_moedas_25:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_moedas_25 = quantidade_moedas_25 - quantidade_saque
                elif retirar_dinheiro == 11:
                    print("Você escolheu a moeda de R$0.10")
                    print("Há um limite de", quantidade_moedas_10, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_moedas_10:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_moedas_10 = quantidade_moedas_10 - quantidade_saque
                elif retirar_dinheiro == 12:
                    print("Você escolheu a moeda de R$0.05")
                    print("Há um limite de", quantidade_moedas_5, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_moedas_5:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_moedas_5 = quantidade_moedas_5 - quantidade_saque
                elif retirar_dinheiro == 13:
                    print("Você escolheu a moeda de R$0.01")
                    print("Há um limite de", quantidade_moedas_1centavo, "notas para serem retiradas.")
                    quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    while quantidade_saque > quantidade_moedas_1centavo:
                        print("Não é possível retirar esse valor. Saldo insuficiente.")
                        quantidade_saque = int(input("Quantas cédulas/moedas você deseja retirar? "))
                    quantidade_moedas_1centavo = quantidade_moedas_1centavo - quantidade_saque
                saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)
                escolha_retirar_mais_dinheiro = int(input("Deseja retirar mais dinheiro? Digite 1 para sim e 2 para não: "))
                while escolha_retirar_mais_dinheiro != 1 and escolha_retirar_mais_dinheiro != 2:
                    escolha_retirar_mais_dinheiro = int(input("Digite um valor válido. 1 para sim e 2 para não: "))
            print("---------------------------------------------------------------------")
            print("Quantidade final de notas de 200 reais", quantidade_notas_200)
            print("Quantidade final de notas de 100 reais", quantidade_notas_100)
            print("Quantidade final de notas de 50 reais", quantidade_notas_50)
            print("Quantidade final de notas de 20 reais", quantidade_notas_20)
            print("Quantidade final de notas de 10 reais", quantidade_notas_10)
            print("Quantidade final de notas de 5 reais", quantidade_notas_5)
            print("Quantidade final de notas de 2 reais", quantidade_notas_2)
            print("Quantidade final de moedas de 1 real", quantidade_moedas_1real)
            print("Quantidade final de moedas de 50 centavos", quantidade_moedas_50)
            print("Quantidade final de moedas de 25 centavos", quantidade_moedas_25)
            print("Quantidade final de moedas de 10 centavos", quantidade_moedas_10)
            print("Quantidade final de moedas de 5 centavos", quantidade_moedas_5)
            print("Quantidade final de moedas de 1 centavo", quantidade_moedas_1centavo)

        elif opcao_menu == 3:  # Serve para adicionar refrigerantes à máquina
            refrigerantes_adicionados = 0
            capacidade_refrigerantes = 150
            excedente_refrigerantes = capacidade_refrigerantes - estoque_refrigerante
            adicionar_mais_refrigerantes = 1
            while adicionar_mais_refrigerantes == 1:
                print("A capacidade em estoque é:", capacidade_refrigerantes)
                print("Há", estoque_refrigerante, "refrigerantes no estoque.")
                print("De modo que há espaço para no máximo mais: ", excedente_refrigerantes)
                refrigerantes_adicionados = int(input("Quantos refrigerantes você gostaria de adicionar? "))
                if refrigerantes_adicionados <= excedente_refrigerantes:
                    print("----------------------------------------------------------------------")
                    print("O seu estoque ficou com", refrigerantes_adicionados + estoque_refrigerante, "refrigerantes, sendo a capacidade total de: ", capacidade_refrigerantes)
                    print("----------------------------------------------------------------------")
                    estoque_refrigerante = estoque_refrigerante + refrigerantes_adicionados
                    excedente_refrigerantes = capacidade_refrigerantes - estoque_refrigerante
                    adicionar_mais_refrigerantes = int(input("gostaria de adicionar mais refrigerantes? 1 para sim e 2 para não: "))
                elif refrigerantes_adicionados > excedente_refrigerantes:
                    print("-----------------------------------------------")
                    print("Essa quantidade pretendida não cabe no estoque.")
                    adicionar_mais_refrigerantes = int(input("gostaria de adicionar mais refrigerantes? 1 para sim e 2 para não: "))
                    print("-----------------------------------------------")
            print("------------------------------------------------------------")
            print("Você adicionou", refrigerantes_adicionados, "e a quantidade atualizada em estoque é: ", estoque_refrigerante)
            print("------------------------------------------------------------")

        elif opcao_menu == 4:  # serve para o administrador retirar refrigerantes da máquina sem ter que pagar
            retirar_mais_refrigerantes = 1
            while retirar_mais_refrigerantes == 1:
                print("Quantidade de refrigerantes em estoque:", estoque_refrigerante)
                refrigerantes_retirados = int(input("Quantos refrigerantes você gostaria de retirar? "))
                if refrigerantes_retirados > estoque_refrigerante:
                    print("-------------------------------------------------------------------")
                    print("No estoque há apenas", estoque_refrigerante, "refrigerantes.")
                    print("Não há itens suficientes em estoque para fazer a retirada desejada.")
                    print("-------------------------------------------------------------------")
                else:
                    estoque_refrigerante = estoque_refrigerante - refrigerantes_retirados
                    print("-------------------------------------------------------------------")
                    retirar_mais_refrigerantes = int(input("Deseja retirar mais unidades? Digite 1 para Sim e 2 para Não: "))
                    print("-------------------------------------------------------------------")
            print("A quantidade atualizada em estoque é: ", estoque_refrigerante)
            print("------------------------------------------------------------")

        elif opcao_menu == 5:  # Serve para mostrar o valor total em dinheiro dentro da máquina, e a quantidade de refrigerantes em estoque.
            print("------------------------------------------------------------------------")
            print("O valor total em cédulas e moedas dentro da máquina é: R$", saldo_maquina)
            print("A quantidade total de refrigerantes dentro da máquina é: ", estoque_refrigerante)
            print("------------------------------------------------------------------------")

        elif opcao_menu == 6:  # Serve para mostrar a quantidade que tem de cada cédula/moeda dentro da máquina
            print()            
            print("-----------------------------------------------------------")
            print()
            print("--CONTROLE DAS CÉDULAS E MOEDAS DA MÁQUINA:--")  
            print("Quantidade de notas de 200 reais:", quantidade_notas_200)
            print("Quantidade de notas de 100 reais:", quantidade_notas_100)
            print("Quantidade de notas de 50 reais:", quantidade_notas_50)
            print("Quantidade de notas de 20 reais:", quantidade_notas_20)
            print("Quantidade de notas de 10 reais:", quantidade_notas_10)
            print("Quantidade de notas de 5 reais:", quantidade_notas_5)
            print("Quantidade de notas de 2 reais:", quantidade_notas_2)
            print("Quantidade de moedas de 1 real:", quantidade_moedas_1real)
            print("Quantidade de moedas de 50 centavos:", quantidade_moedas_50)
            print("Quantidade de moedas de 25 centavos:", quantidade_moedas_25)
            print("Quantidade de moedas de 10 centavos:", quantidade_moedas_10)
            print("Quantidade de moedas de 5 centavos:", quantidade_moedas_5)
            print("Quantidade de moedas de 1 centavo:", quantidade_moedas_1centavo)
            print("-----------------------------------------")



    # PARTE DO CONSUMIDOR:


    elif nivel_acesso == 2:

        if estoque_refrigerante > 0:  # garante que não vai permitir uma transação se a máquina não tiver refrigerante em estoque para fornecer para o consumidor 

            # Boas vindas e notas que serão aceitas:
            print()            
            print("-----------------------------------------------------------")
            print("Olá, seja bem vindo!")
            print("O preço do refrigerante é R$", preco_refrigerante)
            print("Esta máquina aceita notas de R$200, R$100, R$50, R$20, R$10, R$5 e R$2; e moedas de R$1, R$0.50, R$0.25, R$0.10, R$0.05 e R$0.01")         
            print("-----------------------------------------------------------")
            print()

            # primeira parte garante que o valor inserido seja válido
            valor_inserido = float(input("Quanto deseja inserir? "))
            while valor_inserido != 200 and valor_inserido != 100 and valor_inserido != 50 and valor_inserido != 20 and valor_inserido != 10 and valor_inserido != 5 and valor_inserido != 2 and valor_inserido != 1 and valor_inserido != 0.5 and valor_inserido != 0.25 and valor_inserido != 0.10 and valor_inserido != 0.05 and valor_inserido != 0.01:
                valor_inserido = float(input("Valor inválido. Insira um valor válido: "))
            valor_total_inserido = valor_total_inserido + valor_inserido

            # atualização do saldo do moedeiro a partir da primeira entrada de dinheiro:
            if valor_inserido == 200:   
                quantidade_notas_200 = quantidade_notas_200 + 1
            elif valor_inserido == 100:
                quantidade_notas_100 = quantidade_notas_100 + 1
            elif valor_inserido == 50:
                quantidade_notas_50 = quantidade_notas_50 + 1
            elif valor_inserido == 20:
                quantidade_notas_20 = quantidade_notas_20 + 1
            elif valor_inserido == 10:
                quantidade_notas_10 = quantidade_notas_10 + 1
            elif valor_inserido == 5:
                quantidade_notas_5 = quantidade_notas_5 + 1
            elif valor_inserido == 2:
                quantidade_notas_2 = quantidade_notas_2 + 1
            elif valor_inserido == 1:
                quantidade_moedas_1real = quantidade_moedas_1real + 1
            elif valor_inserido == 0.5:
                quantidade_moedas_50 = quantidade_moedas_50 + 1
            elif valor_inserido == 0.25:
                quantidade_moedas_25 = quantidade_moedas_25 + 1
            elif valor_inserido == 0.10:
                quantidade_moedas_10 = quantidade_moedas_10 + 1
            elif valor_inserido == 0.05:
                quantidade_moedas_5 = quantidade_moedas_5 + 1
            elif valor_inserido == 0.01:
                quantidade_moedas_1centavo = quantidade_moedas_1centavo + 1
            saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)


            # ao passo em que o valor inserido foi atualizado no moedeiro, vamos ter 2 cenários:

            # 1 - o dinheiro já foi suficiente
            if valor_total_inserido >= preco_refrigerante:
                troco = valor_total_inserido - preco_refrigerante
                estoque_refrigerante = estoque_refrigerante - 1
                print("Aqui está o seu refrigerante e o seu troco, que é de R$", troco)

                # atualização do saldo do moedeiro a partir das saídas para o troco (se houver):
                while troco >= 200:
                    quantidade_notas_200 = quantidade_notas_200 - 1
                    troco = troco - 200
                while troco >= 100:
                    quantidade_notas_100 = quantidade_notas_100 - 1
                    troco = troco - 100
                while troco >= 50:
                    quantidade_notas_50 = quantidade_notas_50 - 1
                    troco = troco - 50
                while troco >= 20:
                    quantidade_notas_20 = quantidade_notas_20 - 1
                    troco = troco - 20
                while troco >= 10:
                    quantidade_notas_10 = quantidade_notas_10 - 1
                    troco = troco - 10
                while troco >= 5:
                    quantidade_notas_5 = quantidade_notas_5 - 1
                    troco = troco - 5
                while troco >= 2:
                    quantidade_notas_2 = quantidade_notas_2 - 1
                    troco = troco - 2
                while troco >= 1:
                    quantidade_moedas_1real = quantidade_moedas_1real - 1
                    troco = troco - 1
                while troco >= 0.5:
                    quantidade_moedas_50 = quantidade_moedas_50 - 1
                    troco = troco - 0.5
                while troco >= 0.25:
                    quantidade_moedas_25 = quantidade_moedas_25 - 1
                    troco = troco - 0.25
                while troco >= 0.10:
                    quantidade_moedas_10 = quantidade_moedas_10 - 1
                    troco = troco - 0.10
                while troco >= 0.05:
                    quantidade_moedas_5 = quantidade_moedas_5 - 1
                    troco = troco - 0.05
                while troco >= 0.01:
                    quantidade_moedas_1centavo = quantidade_moedas_1centavo - 1
                    troco = troco - 0.01
                saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)

            # 2 o dinheiro não foi suficiente
            else:
                sair_repeticao = 100  # variável de controle para terminar a transação no caso de o usuário estar com saldo insuficiente e não querer complementar
                while preco_refrigerante > valor_total_inserido and sair_repeticao != preco_refrigerante:
                    escolha = 0
                    while escolha != 1 and escolha != 2:
                        escolha = int(input("O dinheiro ainda é insuficiente. Deseja inserir mais dinheiro? Digite 1 para sim e 2 para não: "))

                # 2.1 o dinheiro não foi suficiente e decidiu complementar
                        if escolha == 1:
                            print("Você escolheu adicionar mais dinheiro.")
                            soma_complemento = 0
                            while valor_total_inserido < preco_refrigerante:
                                complemento = float(input("Insira um valor para complementar: ")) 
                                while complemento != 200 and complemento != 100 and complemento != 50 and complemento != 20 and complemento != 10 and complemento != 5 and complemento != 2 and complemento != 1 and complemento != 0.5 and complemento != 0.25 and complemento != 0.10 and complemento != 0.05 and complemento != 0.01:
                                    print("valor inválido. Insira um valor válido: ")
                                    complemento = float(input("Quanto deseja inserir? "))
                                valor_total_inserido = valor_total_inserido + complemento
                                if complemento == 200 or complemento == 100 or complemento == 50 or complemento == 20 or complemento == 10 or complemento == 5 or complemento == 2 or complemento == 1 or complemento == 0.5 or complemento == 0.25 or complemento == 0.1 or complemento == 0.05 or complemento == 0.01:
                                    soma_complemento = soma_complemento + complemento
                                if complemento == 200:
                                    quantidade_notas_200 = quantidade_notas_200 + 1
                                elif complemento == 100:
                                    quantidade_notas_100 = quantidade_notas_100 + 1
                                elif complemento == 50:
                                    quantidade_notas_50 = quantidade_notas_50 + 1
                                elif complemento == 20:
                                    quantidade_notas_20 = quantidade_notas_20 + 1
                                elif complemento == 10:
                                    quantidade_notas_10 = quantidade_notas_10 + 1
                                elif complemento == 5:
                                    quantidade_notas_5 = quantidade_notas_5 + 1
                                elif complemento == 2:
                                    quantidade_notas_2 = quantidade_notas_2 + 1
                                elif complemento == 1:
                                    quantidade_moedas_1real = quantidade_moedas_1real + 1
                                elif complemento == 0.5:
                                    quantidade_moedas_50 = quantidade_moedas_50 + 1
                                elif complemento == 0.25:
                                    quantidade_moedas_25 = quantidade_moedas_25 + 1
                                elif complemento == 0.10:
                                    quantidade_moedas_10 = quantidade_moedas_10 + 1
                                elif complemento == 0.05:
                                    quantidade_moedas_5 = quantidade_moedas_5 + 1
                                elif complemento == 0.01:
                                    quantidade_moedas_1centavo = quantidade_moedas_1centavo + 1
                            saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)
                        
                            troco = valor_total_inserido - preco_refrigerante
                            estoque_refrigerante = estoque_refrigerante - 1
                            print("Aqui está o seu refrigerante e o seu troco de R$", troco)

                                # atualização do saldo do moedeiro a partir de saídas de troco:
                            while troco >= 200:
                                quantidade_notas_200 = quantidade_notas_200 - 1
                                troco = troco - 200
                            while troco >= 100:
                                quantidade_notas_100 = quantidade_notas_100 - 1
                                troco = troco - 100
                            while troco >= 50:
                                quantidade_notas_50 = quantidade_notas_50 - 1
                                troco = troco - 50
                            while troco >= 20:
                                quantidade_notas_20 = quantidade_notas_20 - 1
                                troco = troco - 20
                            while troco >= 10:
                                quantidade_notas_10 = quantidade_notas_10 - 1
                                troco = troco - 10
                            while troco >= 5:
                                quantidade_notas_5 = quantidade_notas_5 - 1
                                troco = troco - 5
                            while troco >= 2:
                                quantidade_notas_2 = quantidade_notas_2 - 1
                                troco = troco - 2
                            while troco >= 1:
                                quantidade_moedas_1real = quantidade_moedas_1real - 1
                                troco = troco - 1
                            while troco >= 0.5:
                                quantidade_moedas_50 = quantidade_moedas_50 - 1
                                troco = troco - 0.5
                            while troco >= 0.25:
                                quantidade_moedas_25 = quantidade_moedas_25 - 1
                                troco = troco - 0.25
                            while troco >= 0.10:
                                quantidade_moedas_10 = quantidade_moedas_10 - 1
                                troco = troco - 0.10
                            while troco >= 0.05:
                                quantidade_moedas_5 = quantidade_moedas_5 - 1
                                troco = troco - 0.05
                            while troco >= 0.01:
                                quantidade_moedas_1centavo = quantidade_moedas_1centavo - 1
                                troco = troco - 0.01
                            saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)


                # 2.2 dinheiro não foi suficiente e não quis completar:
                        else:
                            print("--------------------------------------------------------")
                            print("A transação não foi concluída. Você havia inserido R$", valor_total_inserido, "Aqui está o seu dinheiro de volta")
                            sair_repeticao = preco_refrigerante 
                            troco = valor_total_inserido
                            while troco >= 200:
                                quantidade_notas_200 = quantidade_notas_200 - 1
                                troco = troco - 200
                            while troco >= 100:
                                quantidade_notas_100 = quantidade_notas_100 - 1
                                troco = troco - 100
                            while troco >= 50:
                                quantidade_notas_50 = quantidade_notas_50 - 1
                                troco = troco - 50
                            while troco >= 20:
                                quantidade_notas_20 = quantidade_notas_20 - 1
                                troco = troco - 20
                            while troco >= 10:
                                quantidade_notas_10 = quantidade_notas_10 - 1
                                troco = troco - 10
                            while troco >= 5:
                                quantidade_notas_5 = quantidade_notas_5 - 1
                                troco = troco - 5
                            while troco >= 2:
                                quantidade_notas_2 = quantidade_notas_2 - 1
                                troco = troco - 2
                            while troco >= 1:
                                quantidade_moedas_1real = quantidade_moedas_1real - 1
                                troco = troco - 1
                            while troco >= 0.5:
                                quantidade_moedas_50 = quantidade_moedas_50 - 1
                                troco = troco - 0.5
                            while troco >= 0.25:
                                quantidade_moedas_25 = quantidade_moedas_25 - 1
                                troco = troco - 0.25
                            while troco >= 0.10:
                                quantidade_moedas_10 = quantidade_moedas_10 - 1
                                troco = troco - 0.10
                            while troco >= 0.05:
                                quantidade_moedas_5 = quantidade_moedas_5 - 1
                                troco = troco - 0.05
                            while troco >= 0.01:
                                quantidade_moedas_1centavo = quantidade_moedas_1centavo - 1
                                troco = troco - 0.01
                            saldo_maquina = (quantidade_notas_200 * 200) + (quantidade_notas_100 * 100) + (quantidade_notas_50 * 50) + (quantidade_notas_20 * 20) + (quantidade_notas_10 * 10) + (quantidade_notas_5 * 5) + (quantidade_notas_2 * 2) + (quantidade_moedas_1real * 1) + (quantidade_moedas_50 * 0.5) + (quantidade_moedas_25 * 0.25) + (quantidade_moedas_10 * 0.10) + (quantidade_moedas_5 * 0.05) + (quantidade_moedas_1centavo * 0.01)
                    
            print("-----------------------------------------------------------")
            print("--CONTROLE DAS TRANSAÇÕES DA MÁQUINA:--")  # esta parte não estaria visível para o usuário na prática, está aqui apenas se tratando de recurso para deixar mais fácil de ver o funcionamento do código ao final
            print("Quantidade final de notas de 200 reais", quantidade_notas_200)
            print("Quantidade final de notas de 100 reais", quantidade_notas_100)
            print("Quantidade final de notas de 50 reais", quantidade_notas_50)
            print("Quantidade final de notas de 20 reais", quantidade_notas_20)
            print("Quantidade final de notas de 10 reais", quantidade_notas_10)
            print("Quantidade final de notas de 5 reais", quantidade_notas_5)
            print("Quantidade final de notas de 2 reais", quantidade_notas_2)
            print("Quantidade final de moedas de 1 real", quantidade_moedas_1real)
            print("Quantidade final de moedas de 50 centavos", quantidade_moedas_50)
            print("Quantidade final de moedas de 25 centavos", quantidade_moedas_25)
            print("Quantidade final de moedas de 10 centavos", quantidade_moedas_10)
            print("Quantidade final de moedas de 5 centavos", quantidade_moedas_5)
            print("Quantidade final de moedas de 1 centavo", quantidade_moedas_1centavo)
            print("-----------------------------------------------------------")
            print("Valor total inserido pelo Cliente: R$", valor_total_inserido)
            if valor_total_inserido >= preco_refrigerante:
                print("Troco fornecido: R$", valor_total_inserido - preco_refrigerante)
            else:
                print("Troco fornecido: R$", valor_total_inserido)
            print("Saldo final da máquina: R$", saldo_maquina)
            print("Estoque final da máquina: ", estoque_refrigerante)
            valor_inserido = 0
            valor_total_inserido = 0
        
        else:
            print("-------------------------------------------------------------")
            print("Não há refrigerantes em estoque. Desculpe pelo inconveniente!")