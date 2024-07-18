import json

from trabalhando_json import PATH, Pessoa, as_dump

as_dump()

with open(PATH, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.name, p1.age)
    print(p2.name, p2.age)
    print(p3.name, p3.age)