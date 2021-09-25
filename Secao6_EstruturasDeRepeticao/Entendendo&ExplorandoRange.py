"""
RANGES:
- Precisa-se conhecer loop for para trabalhar com Ranges
- Precisa-se conhecer Ranges para se trabalhar melhor com loop for

    Ranges são usadas para gerar sequencias numéricas, não de forma aleatória, mas de maneira específica.

"""
# FORMAS GERAIS

# Forma 1
# range (valor_de_parada)
# valor de parada não inclusive (inicio padrão 0 e passo de 1 em 1)
for num in range(11):
    print(num)

# Forma 2
# rang(valor_de_inicio, valor_de_parada)
# valor de inicio especificado pelo usuário
for num2 in range(2, 14):
    print(num2)

# Forma 3
# range(valor_de_inicio, valor_de_parada, passo)
# o passo especificado pelo usuário
print('forma 3')
for num3 in range(2, 14, 2):
    print(num3)
print('forma 4')
# Forma 4
# range(valor_de_inicio(desta vez o maior), valor_de_parada(desta vez o menor), passo(- para ser invertido))
# passo especificado pelo usuário, porém invertido, usando sinal de "-"
for num4 in range(50, -1, -5):
    print(num4)
