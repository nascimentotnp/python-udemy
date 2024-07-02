cpf = "110425127$28"


def soma(cpf):
    total = 0
    for digit in cpf:
        if digit.isdigit():
            total += int(digit)

    return total


result = soma(cpf)
print("Sum of CPF digits:", result)
