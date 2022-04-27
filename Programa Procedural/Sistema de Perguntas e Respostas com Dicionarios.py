perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1','b': '2','c': '5', 'd': '4'},
        'resposta_certa': 'd',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 4*2?',
        'respostas': {'a': '6','b': '8','c': '10', 'd': '12'},
        'resposta_certa': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10-5?',
        'respostas': {'a': '5','b': '6','c': '8', 'd': '4'},
        'resposta_certa': 'a',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é a raiz quadrada de 16?',
        'respostas': {'a': '6', 'b': '9', 'c': '4', 'd': '3'},
        'resposta_certa': 'c',
    },

}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    reposta_usuario = input('Digite sua resposta: ')
    while reposta_usuario not in("a","b","c","d"):
        reposta_usuario = input('Digite sua resposta: ')
    if reposta_usuario == pv['resposta_certa']:
        print('Resposta correta!')
        respostas_certas += 1
    else:
        print('Resposta errada.')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = (respostas_certas / qtd_perguntas) * 100
print(f'Voce acertou {respostas_certas} perguntas de {qtd_perguntas} propostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
