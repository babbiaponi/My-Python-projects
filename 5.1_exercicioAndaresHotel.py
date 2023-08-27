"""PROJETO: IMPRIMIR OS ANDARES DO HOTEL, EXCETO O 13º ANDAR
Precisamos imprimir um número para cada andar de um hotel de 20 andares.
Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar."""

#Escreva um código que imprima todos os números exceto o número 13.

numeros = [numero for numero in range(1, 21) if numero != 13]
print(numeros)

#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

contador = 0
while contador<21:
    if contador !=13:
        print ( contador,"º andar",)
    contador = contador +1

contador = 0
for contador in range (1,21):
    if contador != 13:
        print ( contador,"º andar",)

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

contador = 20
while contador>0:
    if contador !=13:
        print ( contador,"º andar",)
    contador = contador -1

contador = 20
while True:
    if contador != 13:
        print ( contador,"º andar",)
    contador -= 1
    if contador < 1:
        break

for contador in range(20, 0, -1):
    if contador != 13:
        print ( contador,"º andar",)

