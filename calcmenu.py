def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: não é possível divisão por zero!"
    return a / b

def elevar_ao_quadrado(a):
    return a ** 2

def menu():
    print("Escolha uma opção:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Elevar ao quadrado")
    print("0 - Sair")

while True:
    menu()
    opcao = input()

    if opcao == '0':
        print("Tchauzinhoo...😘")
        break

    try:
        opcao = int(opcao)
        if opcao == 5:
            n1 = float(input("Digite n1: "))
            print(f"Resultado: {elevar_ao_quadrado(n1)}\n")
        elif opcao in [1, 2, 3, 4]:
            n1 = float(input("Digite n1 : "))
            n2 = float(input("Digite n2: "))

            if opcao == 1:
                print(f"Resultado: {soma(n1, n2)}\n")
            elif opcao == 2:
                print(f"Resultado: {subtracao(n1, n2)}\n")
            elif opcao == 3:
                print(f"Resultado: {multiplicacao(n1, n2)}\n")
            elif opcao == 4:
                print(f"Resultado: {divisao(n1, n2)}\n")
        else:
            print("Opção inválida! Tente novamente.\n")
    except ValueError:
        print("Entrada inválida! Digite um número.\n")
