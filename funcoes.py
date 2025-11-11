from datetime import datetime

def menu():
    menu = '''\n
    *** OPÇÕES ***
    1- Depositar;
    2- Sacar;
    3- Extrato;
    4- Sair;

    Escolha uma opção: '''
    
    return int(input(menu))

def depositar(valor, saldo, historico):
    # if not isinstance(valor, int):
    #     raise ValueError("valor deve ser um numero")
    
    if valor < 0:
        raise ValueError("valor de ser maior que zero")
    
    elif valor > 0:
        saldo += valor
        historico.append({
            "valor": valor,
            "tipo": "Deposito",
            "Data": datetime.now()
        })
        print("\n Deposito realizado com sucesso")

    return saldo, historico

def sacar(valor, saldo, limite, historico):
    # if not isinstance(valor, int):
    #     raise ValueError("valor deve ser um numero")
    
    if valor > saldo:
        raise ValueError("Saldo insuficiente para esse valor")

    elif valor > limite:
        raise ValueError(f"essa conta tem o limite de saque de R${limite},00")

    elif valor > 0:
        saldo -= valor
        historico.append({
            "valor": valor,
            "tipo": "Saque",
            "Data": datetime.now()
        })
        print("\n Saque realizado com sucesso")

    return saldo, historico

def extrato(saldo, historico):
   extrato = {
       "saldo": saldo,
       "historico": tuple(historico)
   }
   print(extrato)
