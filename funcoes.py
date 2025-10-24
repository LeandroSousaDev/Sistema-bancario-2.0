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
    if valor > 0:
        saldo += valor
        historico.append({
            "valor": valor,
            "tipo": "Deposito",
            "Data": datetime.now()
        })
        print("\n Deposito realizado com sucesso")
    else:
        raise ValueError

    return saldo, historico

def sacar(valor, saldo, limite, historico):
    if valor > saldo:
        raise ValueError

    elif valor > limite:
        raise ValueError

    elif valor > 0:
        saldo -= valor
        historico.append({
            "valor": valor,
            "tipo": "Saque",
            "Data": datetime.now()
        })
        print("\n Saque realizado com sucesso")
    else:
        raise ValueError

    return saldo, historico

def extrato(saldo, historico):
   extrato = {
       "saldo": saldo,
       "historico": tuple(historico)
   }
   print(extrato)
