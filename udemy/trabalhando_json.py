import json

PATH = 'saved.json'


class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]


def as_dump():
    with open(PATH, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ELE É O __main__')
    as_dump()
