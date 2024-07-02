def adiciona_clientes(nome, lista=None): #foi definido no parametro que a lista será sempre vazia por padrão
    if lista is None:# logo se eu não passo nada para lista, o código verifica e cria uma nova lista vazia
        lista = []
    lista.append(nome)#se eu passar um valor para a lista ele soma um novo dado a lista
    return lista


cliente1 = adiciona_clientes('luiz')#aqui eu não passo lista no parametro de lista, logo ele cria uma vazia e adiciona o valor
adiciona_clientes('Joana', cliente1)#aqui a lista criada na linha de cima é passada como parametro, logo é adicionado um valor a lista existente
adiciona_clientes('Fernando', cliente1)#aqui eu passo outro parametro e passo lista como parametro, aqui é adicionado um valor àquela lista
cliente1.append('Edu')#aqui é outra abosrdagem, eu ja chamop a lista e adiciono um item a ela

cliente2 = adiciona_clientes('Helena')#aqui eu não passo lista no parametro de lista, logo ele cria uma nova e vazia e adiciona o valor
adiciona_clientes('Maria', cliente2)#repare que aqui eu uso a lista cliente2 criada na linha de cima e não mais cliente1

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)