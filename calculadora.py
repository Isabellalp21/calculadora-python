print("Olá! Eu sou a sua calculadora mágica")

print("Escolha uma operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (x)")
print("4 - Divisão (÷)")

operacao = input("Digite o número da operação: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operacao == "1":
    resultado = numero1 + numero2
    print("Resultado: ", resultado)

elif operacao == "2":
    resultado = numero1 - numero2
    print("Resultado: ", resultado)

elif operacao == "3":
    resultado = numero1 * numero2
    print("Resultado: ", resultado)

elif operacao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado: ", resultado)
    else:
        print("Não posso dividir por zero 😢")

else:
    print("Operação inválida! Tente de novo.")
