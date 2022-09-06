nome = 'Jose Filho'
idade = 26  # int
altura = 1.78  # float
peso = 73
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / (altura) ** 2


print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')