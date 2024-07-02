def executa(funcao, *args):
    return funcao(*args)


def soma(a, b):
    return a + b


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero*multiplicador
    return multiplica


print(
    executa(
        lambda x, y: x + y,
        2, 3
    )
)

#lambda na representação seria o def na declaração da função, os parametros seriam o que esta dentro da função
#soma (x, y) ficando lambda x, y: os dois pontos é pra finalizar a linha def soma(x, y): ficando lambda x, y:
# dentro do lambda não existe return logo o que seria o return para lambda fica após os dois pontos : x+y
# após as vírgulas entraram os valores que quero usar

# def soma(a, b): return a + b   soma(2, 3)  ->  lambda x, y: a + b, 2, 3 importante
