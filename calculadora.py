

class Calculadora(object):
    def __init__(self) -> None:
        pass
        
        
        
    def soma(self):
        a = float(input("Entre com o numero: "))
        b = float(input("Entre com o numero: "))
        resultado = a + b
        print(f'O resultado é {resultado}')

    def multiplicacao(self):
        a = float(input("Entre com o numeros: "))
        b = float(input("Entre com o numero: "))
        resultado = a * b
        print(f'O resultado é {resultado}')
    
    def subtracao(self):
        a = float(input("Entre com o numeros: "))
        b = float(input("Entre com o numero: "))
        resultado = a - b
        print(f'O resultado é {resultado}')
    
    def divisao(self):
        a = float(input("Entre com o dividendo: "))
        b = float(input("Entre com o divisor: "))
        resultado = a / b
        print("o resultado é {:.2f}".format(resultado))
