def hello_world():
    return "hello world!"

def mestre(funcao):
    return funcao()

executando = mestre(hello_world)
print(executando)
print(hello_world())


def master(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def say_hi(name):
    return f"Hi {name}"

def salutation(name, salutation):
    return f"{salutation} {name}"

executar = master(say_hi, "Luiz")
executar2 = master(salutation, "Luiz", salutation="Good Morning")
print(executar)
print(executar2)