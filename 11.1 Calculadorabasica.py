"""Faça uma função calculadora de dois números com três parâmetros: 
os 2 primeiros serão os números da operação e o 3º será a entrada que definirá a operação a ser executada. 
Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
Caso seja inserido um número de operação que não exista, o resultado deverá ser 0."""

def calc (num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4 and num2 != 0:
        return num1 / num2
    else:
        return 0
    
num1 = float(input("Informe o 1º número:"))
num2 = float(input("Informe o 2º número:"))
operacao = int(input("Escolha (1 = Soma, 2 = Subtração, 3 = Multiplicação, 4 = Divisão):"))
resultado = calc (num1, num2, operacao)
print("Resultado:", resultado)
