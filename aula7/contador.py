from itertools import groupby

alunos = [
        {'nome': 'Luiz', 'nota': 'A'},
        {'nome': 'Letícia', 'nota': 'B'},
        {'nome': 'Fabricio', 'nota': 'A'},
        {'nome': 'Rosemary', 'nota': 'C'},
        {'nome': 'Joana', 'nota': 'D'},
        {'nome': 'João', 'nota': 'A'},
        {'nome': 'Eduardo', 'nota': 'B'},
        {'nome': 'André', 'nota': 'A'},
        {'nome': 'Anderson', 'nota': 'C'},
        {'nome': 'josé', 'nota': 'B'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in  alunos_agrupados:
    print(f'agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} alunos tiraram a nota  {agrupamento}')