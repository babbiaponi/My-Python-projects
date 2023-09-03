"""Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, 
no ano atual (2022). Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema 
informará o erro e continuará perguntando até que um valor correto seja preenchido."""

def idade(anoNascimento):
    anoAtual = 2022
    idade = anoAtual - anoNascimento
    return idade

def anoValido():
    while True:
        try:
            anoNascimento = int(input("Digite o ano de nascimento entre 1922 e 2021:"))
            if 1922 <= anoNascimento <= 2021:
                return anoNascimento
            else:
                print("Ano inválido. Por favor, tente novamente.")
        except:
            print("Por favor, digite um valor numérico válido.")

idade = idade
nome_completo = input("Digite seu nome completo: ")
anoNascimento = anoValido()

print("nome:",nome_completo)
print("sua data de nascimento:", anoNascimento)
print(f"Idade em 2022: {idade(anoNascimento)} anos")