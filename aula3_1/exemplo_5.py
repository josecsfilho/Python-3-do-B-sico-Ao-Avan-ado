print()
print('Projeto básico, a fins de educacional')
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '4','b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

        resposta_usuario = input('Sua resposta')

        if resposta_usuario == pv ['resposta_certa']:
            print('EHHHHHH!!!! Você acertou!!!')
            respostas_certas += 1
        else:
            print('IXIIIII!!!! Você ERROU!!')

        print()

qtd_perguntas = len(perguntas)
porcetagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcetagem de acerto foi de {porcetagem_acerto}%.')