#Faça um programa que imprima os números de um 1 até 1000 e ao final deve verificar o tempo que cada um leva para ser executado

import time
inicio=time.time()


for i in range(1001):    
    print(i)
fim = time.time()


diferenca = fim - inicio

print('O tempo de execução foi: ',diferenca)
