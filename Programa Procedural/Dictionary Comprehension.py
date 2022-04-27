lista = [
    ('chave', 'valor'),
    ('chave1', 'valor2'),
]

d1 = {x: y for x, y in lista}
print(d1)

d2 = {x: y for x, y in enumerate(range(5))}
print(d2)

d3 = {f'chave{x}': x**2 for x in range(5)}
print(d3)