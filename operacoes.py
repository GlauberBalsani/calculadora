from calculadora import Calculadora


class Operacoes:
    def __init__(self) -> None:
        pass
    
    
    def boas_vindas(self):
        print("***********************")
        print("*Bem vindo a Calculadora*")
        print("************************")
        print()

    def menu(self):
        operacao = Calculadora()
        try:
            opc = int(input("Escolha sua operação: 1 adição - 2 multiplicação - 3 subtração - 4 divisão: "))
            print('********************')
            if opc == 1:
                print("Soma")
                print("****")
                operacao.soma()
                    
            if opc == 2:
                print("Multiplicação")
                print("**************")
                operacao.multiplicacao()
                    
            if opc == 3:
                print("Subtração")
                print("**********")
                operacao.subtracao()

            if opc == 4:
                print("Divisão")
                print("*******")
                operacao.divisao()
        except ValueError as erro:
            print('Sómente numeros tente de novo..')
            print()
                

