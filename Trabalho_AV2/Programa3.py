###################################
#Daniel Soares Oliveira da Silva  #
#202102410241                     #
#Programa 3                       #
###################################

from cmath import sin
import math

def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Soma: ",x+y)

def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Subtracao: ",x-y)

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Multiplicacao: ",x*y)

def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ",x/y)
    
def seno():
    a = float(input("Digite o ângulo: "))
    print("Seno: ",math.sin(a))
    
def raiz_quadrada():
    x = int(input("Digite o número: "))
    print("Raiz: ",math.isqrt(x))
    
def exponecial():
    x = float(input("Digite o número: "))
    print("Raiz: ",math.exp(x))

opcao=1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print("5. Seno ")
    print("6. Raiz ")
    print("7. Exponecial ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()
    if(opcao==5):
        seno()
    if(opcao==6):
        raiz_quadrada()
    if(opcao==7):
        exponecial()