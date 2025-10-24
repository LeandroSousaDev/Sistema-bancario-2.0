import funcoes


def main():
    saldo = 0
    limite = 500
    historico = []

    resposta = '''
    Requistos
        - O Valor deve ser um numero
        - O valor deve ser positivo            
    '''

    resposta2 = f'''
    Reqisitos
        - O valor deve ser um numero
        - O valor deve ser positivo
        - O valor não deve utrapassar o limite de: {limite},00
    '''

    while True:

        opcao = funcoes.menu()

        if(opcao == 1):
            try:
                valor = int(input("\n Digite o valor que deseja depositar: "))
                saldo, historico = funcoes.depositar(valor=valor, saldo=saldo, historico=historico)
            except ValueError:
                print(resposta)
                
        
        elif(opcao == 2):
            try:
                valor = int(input("\n Digite o valor que deseja sacar: "))
                saldo, historico = funcoes.sacar(saldo=saldo, limite=limite, valor=valor, historico=historico)
            except ValueError:
                print(resposta2)

        elif(opcao == 3):
            funcoes.extrato(saldo=saldo, historico=historico)

        elif(opcao == 4):
            break

        else:
            print("\n Opção invalida")

main()