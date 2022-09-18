

#def saudacao(saudacao, nome):
#   print(f'{saudacao} {nome}')

#saudacao('Olá', 'Joãozinho')
#saudacao('Oi', 'Maria')
#saudacao('Hey', 'Eduardo')

#def soma(n1, n2, n3)
#    print(n1 + n2 + n3)

#soma(2, 1, 3)
#soma 1, 1, 1)
#soma(2, 1, 1)

#def aumento_percentual(valor, percentual):
#   return valor + (valor * percentual / 100)

#ap = aumento_percentual(50, 10)
#print(ap)
#ap = aumento_percentual(100, 10)
#print(ap)
#ap = aumento_percentual(10, 10)
#print(ap)
#ap = aumento_percentual(15, 100)
#print(ap)

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizz, {n} é divisível por 3 e 5'
    elif n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    elif n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n

from random import  randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))