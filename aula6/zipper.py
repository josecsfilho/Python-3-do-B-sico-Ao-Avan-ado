


cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)

for valor in cidades_estados:
    print(valor[0], valor[1])