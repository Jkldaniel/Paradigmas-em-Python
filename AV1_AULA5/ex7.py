#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Primeiro numero: '))
n2  = int(input('Segundo numero : '))
n3 = int(input('Terceiro numero: '))

#Calculando o maior número
maior = n1

if (n2 > maior):
       maior = n2
if (n3 > maior):
        maior = n3

print('Maior: ',maior)

#Calculando o menor número
menor = n1

if (n2 < menor):
        menor = n2
if (n3 < menor):
        menor = n3

print('Menor: ',menor)