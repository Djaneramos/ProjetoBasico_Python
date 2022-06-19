from random import randint

def jogo(d):
    adivinhe = randint(1,d)
    count = 0
    numero = 0

    while numero!= adivinhe:
        numero = int(input(f'Informe um numero de 1 a {d} para saber em quantas tentativas você acerta o numero escolhido pela maquina '))

        if numero > adivinhe:
            print('Chutou um valor alto, tente novamente \n')
        elif numero < adivinhe:
            print('Chutou um valor baixo,tente mais uma vez \n') 
          
        count +=1

    print('Você acertou. O numero sorteado foi: {}'.format(numero))
    print(f'Você acertou  na {count} tentativas')
    
jogo(50)       
