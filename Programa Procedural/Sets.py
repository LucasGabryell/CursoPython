#Sets não tem elementos repetidos
#União |
#add(adicionar), update(atualizar), clear(limpar), discard(eliminar um ou mais elementos)
#Ambos & (elemento presente nos dois sets)
#difference - (elemento que esta apenas no set da esquerda)
#symmetric_difference ^ (Elementos unicos de cada set)
s1 = {1,2,3,4,5}

for v in s1:
    print(v)

s1.discard(2)
print(s1)
s1.add(7)
print(s1)

s2 = set()
s2.update('P','Y','T','H','O','N')
print(s2)

l1 = [1,2,1,3,4,5,1,4,1,1,2,1,7,8,9,'Lucas', 'Lucas']
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s1 ^ s2
print(s3)