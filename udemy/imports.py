def criar_funcao(func):
    def wrapper(*args, **kwargs):
        print(f"Antes da função")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"Depois da função {resultado}")
        return resultado

    return wrapper


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(arg):
    if not isinstance(arg, str):
        raise TypeError("Apenas strings são aceitas")


invertida = inverte_string('123')

print(inverte_string(invertida))
