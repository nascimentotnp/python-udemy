from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total = 0


# for produto in produtos:
#     total += produto['preco']
# print(total)

# total = sum([produto['preco'] for produto in produtos])
# print(total)

# def funcao_reduce(acumulador, produto):
#     return acumulador + produto['preco']


total = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos, 0)
print(total)
