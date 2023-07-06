menu = '''
----------------Olá cliente, seja bem-vindo----------------------
--------------Por favor, selecione a opção desejada--------------
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair
'''
saldo = 0
limite = 500
extrato = " "
numero_saques = 0
saque_diario = 3

while True:
    opcao = input(menu)
    if (opcao.upper()) == "D":
        dinheiro = float(input("Por favor, digite o valor que deseja depositar em sua conta: "))
        print("Depósito realizado com sucesso!!")
        if dinheiro > 0:
            saldo += dinheiro
            extrato += f"Depósito no valor de R$ {dinheiro:.2f}\n"
            
        else:
            print("Operação não concluída!! Valor informado incorreto.")
            
    elif (opcao.upper()) == "S":
        dinheiro = float(input("Por favor, digite o valor que deseja sacar: "))
        
        excedeu_saldo = dinheiro > saldo
        excedeu_limite = dinheiro > limite
        excedeu_saque = numero_saques >= saque_diario
        
        if excedeu_limite:
            print("Operação não concluída!! Valor informado maior que o limite de saque, por gentileza, escolha um valor menor!")       
            
        
        elif excedeu_saldo:
            print("Operação não concluída!! Valor informado maior que seu saldo bancário, por gentileza, escolha outro valor!")
            
        
        elif excedeu_saque:
            print("Operação não concluída!! Você excedeu a quantidade de saque diário, por gentileza, volte amanhã!")
            
        
        elif dinheiro > 0:
            saldo -= dinheiro
            extrato += f"Saque no valor de R$ {dinheiro: .2f}\n"
            numero_saques += 1
        
        else:
            print("Operação não concluída!! Valor informado é inválido, por gentileza, escolha outro valor!")
        
    elif (opcao.upper()) == "E":
        print(f"""
----------------------- Olá cliente ---------------------

-------------------- Extrato bancário ------------------


-----Seu saldo é de: R$ {saldo: .2f}.-----
-----Você já fez: {numero_saques} saques diáros.-----
-----Você ainda possui {saque_diario - numero_saques} saques diários-----


---------------------------------------------------------
----------------- Histórico de transações ---------------

{extrato}

---------------------------------------------------------
""")
    
    elif opcao.upper() == "Q":
        print("""
----------------------------------------------------------------------------
------------------- Somos gratos por você ser nosso cliente ----------------
----------------------------------------------------------------------------
-------------------------- Tenha um excelente dia --------------------------
----------------------------------------------------------------------------

""")
        break
    else:
        print("Opção inválida!! Por favor selecione uma opção válida.")
