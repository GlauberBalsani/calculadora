

def boas_vindas():
    print("***********************")
    print("*Bem vindo a Calculadora*")
    print("************************")

def menu():
    try:
        opc = int(input("Escolha sua operação: 1 adição - 2 multiplicação - 3 subtração - 4 divisão: "))
        print('********************')
        if opc == 1:
            print("Soma")
            print("****")
            soma()
                
        if opc == 2:
            print("Multiplicação")
            print("**************")
            multiplicacao()
                
        if opc == 3:
            print("Subtração")
            print("**********")
            subtracao()

        if opc == 4:
            print("Divisão")
            print("*******")
            divisao()
    except ValueError as erro:
        print('Sómente numeros tente de novo..')
        print()
        menu()    



print()


def soma():
    a = float(input("Entre com o numero: "))
    b = float(input("Entre com o numero: "))
    resultado = a + b
    print("o resultado é {}".format(resultado))

def multiplicacao():
    a = float(input("Entre com o numeros: "))
    b = float(input("Entre com o numero: "))
    resultado = a * b
    print("o resultado é {:.2f}".format(resultado))

def subtracao():
    a = float(input("Entre com o numeros: "))
    b = float(input("Entre com o numero: "))
    resultado = a - b
    print("o resultado é {:.2f}".format(resultado))

def divisao():
    a = float(input("Entre com o dividendo: "))
    b = float(input("Entre com o divisor: "))
    resultado = a / b
    print("o resultado é {:.2f}".format(resultado))
    

if __name__=='__main__':
    boas_vindas()
    menu()
       

            
                
    
     
           