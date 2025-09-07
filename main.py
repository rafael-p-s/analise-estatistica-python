from os import remove


def menu():
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICACAO")
    print("4 - DIVISÃO")
    print("0 - Sair")
    respMenu = int(input("Informe o número da operação: "))

    if respMenu == 1:
        return soma()
    elif respMenu == 2:
        return subtracao()
    elif respMenu == 3:
        return multiplicacao()
    elif respMenu == 4:
        return divisao()
    elif respMenu == 0:
        print("Saindo...")
    else:
        print("Informe um número do menu...")
        return menu()


def soma():
    print("SOMA")

    try:
        qtdNumber = int(input("Quantos números deseja somar ? "))
    except ValueError:
        return checkVar("error", soma)

    if qtdNumber < 2:
        print("A soma precisa de pelo menos 2 números.")
        return soma()

    qtdNumber = checkVar(qtdNumber, soma)

    numbers = []
    for i in range(qtdNumber):
        numero = float(input(f"Informe o {i + 1}° número: "))
        numbers.append(numero)
    resultado = sum(numbers)
    print(f"A soma é: {resultado}")

    subMenu(soma)


def subtracao():
    print("Subtração")
    try:
        qtdNumber = int(input("Quantos números deseja subtrair ? "))
    except ValueError:
        return checkVar("error", subtracao)

    if qtdNumber < 2:
        print("A subtração precisa de pelo menos 2 números.")
        return subtracao()

    qtdNumber = checkVar(qtdNumber, subtracao)

    numbers = []
    for i in range(qtdNumber):
        numero = float(input(f"Informe o {i + 1}° número: "))
        numbers.append(numero)

    resultado = numbers[0]
    for n in numbers[1:]:
        resultado -= n

    print(f"A subtração é: {resultado}")

    subMenu(subtracao)


def multiplicacao():
    print("Multiplicação")
    try:
        qtdNumber = int(input("Quantos números deseja multiplicar ? "))
    except ValueError:
        return checkVar("error", multiplicacao)

    if qtdNumber < 2:
        print("A multiplicação precisa de pelo menos 2 números.")
        return multiplicacao()

    qtdNumber = checkVar(qtdNumber, multiplicacao)

    numbers = []
    for i in range(qtdNumber):
        numero = float(input(f"Informe o {i + 1}° número: "))
        numbers.append(numero)

    resultado = numbers[0]
    for n in numbers[1:]:
        resultado *= n

    print(f"A multiplicação é: {resultado}")

    subMenu(multiplicacao)

def divisao():
        print("Divisão")
        try:
            qtdNumber = int(input("Quantos números deseja dividir ? "))
        except ValueError:
            return checkVar("error", divisao)

        if qtdNumber < 2:
            print("A divisão precisa de pelo menos 2 números.")
            return divisao()

        qtdNumber = checkVar(qtdNumber, divisao)

        numbers = []
        for i in range(qtdNumber):
            numero = float(input(f"Informe o {i + 1}° número: "))
            numbers.append(numero)

        resultado = numbers[0]
        for n in numbers[1:]:
            resultado /= n

        print(f"A divisão é: {resultado}")

        subMenu(divisao)


def checkVar(qtdNumber, origen):
    if isinstance(qtdNumber, (float, str)) or qtdNumber == "error":
        print("Informe somente números inteiros...")
        return origen()
    return qtdNumber


def subMenu(origen):
    print(" ")
    resp = int(input("Se deseja continuar digite 1 ----- Voltar par ao menu digite 2 ----- Sair digite 0 (zero)"))
    if resp == 1:
        return origen()
    elif resp == 2:
        return menu()
    elif resp == 0:
        print("Saindo...")
    else:
        print("Digite penas 1, 2 ou 0")
        return subMenu()


print("Inciando")
menu()
