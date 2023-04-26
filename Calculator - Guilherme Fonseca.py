def soma(a, b):
    decnumr = dec_num + dec_num2
    bin_num3 = bin(decnumr)
    result = bin_num3
    return result


def sub(a, b):
    decnumr = dec_num - dec_num2
    bin_num3 = bin(decnumr)
    result = bin_num3
    return result


def mult(a, b):
    decnumr = dec_num * dec_num2
    bin_num3 = bin(decnumr)
    result = bin_num3
    return result


def div(a, b):
    try:
        decnumr = dec_num / dec_num2
        bin_num3 = bin(int(decnumr))
        result = bin_num3
        return result
    except ZeroDivisionError:
        print("Não existe divisão por zero, por favor tente novamente ")


print("\t\tCalculadora de Binário \n\n Feita por Guilherme Fonseca da Costa\n")

while True:
    bin_num = input("Digite o primeiro número binário: \n")
    bin_num2 = input("Digite o segundo número binário: \n")
    if all(char in "01" for char in bin_num):
        dec_num = int(bin_num, 2)
        dec_num2 = int(bin_num2, 2)
        print("1 - Soma \n")
        print("2 - Subtração \n")
        print("3 - Multiplicação \n")
        print("4 - Divisão \n")
        op = int(input("Seleciona uma operação: \n "))
        if op == 1:
            print(f"{soma(bin_num, bin_num2)}")
        elif op == 2:
            print(f"{sub(bin_num, bin_num2)}")
        elif op == 3:
            print(f"{mult(bin_num, bin_num2)}")
        elif op == 4:
            print(f"{div(bin_num, bin_num2)}")
        else:
            print("Digite apenas os número indicados")
    else:
        print("Utilize apenas 0 e 1")
