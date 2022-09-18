

#def ola_mundo():
#    return  'Olá mundo!'

#def mestre(funcao):
#    return funcao()

#executando = mestre(ola_mundo)
#print(executando)

def mestre(funcao, *arg, **kwargs):
    return  funcao(*arg, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'José')
executando2 = mestre(saudacao, 'José', saudacao='Bom dia!')
print(executando)
print(executando2)