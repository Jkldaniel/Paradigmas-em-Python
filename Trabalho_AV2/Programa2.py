###################################
#Daniel Soares Oliveira da Silva  #
#202102410241                     #
#Programa 2                       #
###################################

def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} AM')
        
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} PM')
        
    else:
        print('Valor inválido. Se quiser sair do programa, digite 25 no campo "Hora".')


while True:
    h = int(input('Hora: '))
    if h == 25: break
    m = int(input('Minuto: '))
    converta(h,m)
    print('='*12)