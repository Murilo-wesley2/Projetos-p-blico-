from arqfile import *
arq='dados.txt'

if arqexiste(arq)==False:
    criararq(arq)

while True:
    nome = str(input('digite seu nome:'))
    if nome.isalpha()==True:
        if len(nome)>=3:
            break
        elif len(nome)<3:
            print('\033[31mnumero de caracteres invalido. minimo 3 caracteres\033[m')
    elif nome.isnumeric()==True or nome.isalnum()==True:
        print('\033[31mdigite apenas letras.\033[m')
    else:
        print(f'\033[31merro no tipo de dado digitado\033[m')
print(f'\033[32mseja bem-vindo {nome}\033[m')
