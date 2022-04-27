d1 = dict(chave1 = 'Valor da chave', chave2= 'Valor de outra chave')
d1['nova chave'] = 'valor da chave'
print(d1)

d2 = {'str': 'valor', 123: 'Outro valor', (1,2,3,4): 'Tupla'}

d2['naoexiste'] = 'agoraexiste'
if 'naoexite' in d1:
    print(d2['naoexiste'])
print(d2)

if d1.get('str') is not None:
    print(d1.get('nova_chave'))
print(123)

print('str' in d2.keys())
print('valor' in d2.values())

for k in d2.items():
    print(k[0], k[1])

#Dicionários dentro de Dicionários
clientes = {
    'Cliente1' : {
        'nome': 'Lucas',
        'sobrenome': 'Romao'
    },
    'Cliente2': {
        'nome': 'Leleo',
        'sobrenome': 'Balao'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')


#Cópia do dicionario

dic1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Lucas', 'Kaio']}
v = dic1.copy()

v[1] = 'Lucas'
v['d'][0] = 'Leleo'

print(dic1)
print(v)

#Lista ou Tupla para dicionario
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

dic = dict(lista)
print(dic)

#Unir os dicionarios

d3 = {
    1: 2,
    2: 3,
    4: 5
}

d4 = {
    'a': 'b',
    'c': 'd'
}

d3.update(d4)
print(d3)

