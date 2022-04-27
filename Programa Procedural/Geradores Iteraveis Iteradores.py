import sys
import time

lista = [0,1,2,3,4,5]
lista = iter(lista)

print(hasattr(lista, '__next__'))

lista2 = list(range(100))
print(sys.getsizeof(lista2))

def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r
g = gera()

for v in g:
    print(v)

