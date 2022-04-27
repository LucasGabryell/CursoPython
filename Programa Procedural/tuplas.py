t1 = (1, 2, 3, "a", "Luiz Otavio")
t2 = (4, 5, 6)
t3 = t1+t2

print(type(t1))
print(t1[2:])
print(t3)

#para alterar uma Tupla

t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)
print(t1)
