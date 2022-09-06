nome = 'Jose Filho'
idade = 26  # int
altura = 1.78  # float
e_maior = idade > 18 # bool
peso = 73
imc = peso / (altura) ** 2

print(nome, 'tem', idade, 'anos, de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))