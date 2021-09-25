"""

Utiliza-se para sair de um loop de maneira projetada.

"""

# EXEMPLO 1:
for numero in range(1, 100):
    if numero == 6:
        break
    else:
        print(numero)
print('Consegui sair do primeiro loop. ')

# EXEMPLO 2:
while True:
    comando = input("Digite 'sair' para sair do loop. ")
    if comando == "sair":
        break
print('Consegui sair do segundo loop. ')
