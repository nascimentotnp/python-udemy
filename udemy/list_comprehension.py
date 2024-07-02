# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = []
#
# for x in fruits:
#   if "a" in x:
#     new_list.append(x)
# ['apple', 'banana', 'mango']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# new_list = [x for x in fruits if "a" in x]
# new_list = [expression for item in iterable if condition == True]

# print(new_list)
# ['apple', 'banana', 'mango']

# A Sintaxe
# new_list = [expression for item in iterable if condition == True]
# O valor de retorno é uma nova lista, deixando a lista antiga inalterada.
# A condição é opcional e pode ser omitida:
#
# Exemplo
# Sem if declaração:
#
# newlist = [x for x in fruits]

# new_list2 = [x for x in range(1, 11)]
# print(new_list2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list_3 = [x.upper() for x in fruits]
# print(new_list_3)
# ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


# new_list_4 = [x if x != "banana" else "orange" for x in fruits]
# print(new_list_4)
# ['apple', 'orange', 'cherry', 'kiwi', 'mango']



symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
# new_list = [expression for item in iterable]

print(codes)