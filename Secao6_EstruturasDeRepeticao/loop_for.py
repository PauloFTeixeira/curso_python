"""
Loop -> estrutura de repetição
For -> uma estrutura desta repetição
    ex.: for item in interavel
            // execução do loop

-------------------------------------------
For = para
in = dentro de...
_ = serve para descartar uma variável desnecessária
-------------------------------------------------------------

Usamos loop para iterar sobre sequencias ou sobre iteráveis

    Exemplos de interaveis
        - string: Ex.: nome = 'Paulo'
        -lista: Ex.: lista = [1, 2, 3, 4, 5]
        -range: Ex.: numero = range (1, 10)
"""
nome = 'Paulo'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)
ponto = '.'

# EXEMPLO 1 DE FOR - ITERANDO SOBRE STRING
for letra in nome:  # TRADUÇÃO - para cada letra nesse numero, imprima ela.
    print(letra)

# EXEMPLO 2 DE FOR - ITERANDO SOBRE LISTA
for num in lista:  # TRADUÇÃO - para cada numero nesta lista, imprima ele.
    print(num)

# EXEMPLO 3 DE FOR - ITERANDO SOBRE RANGE
for num in range(1,10):  # TRADUÇÃO - imprima cada numero dentro da range
    print(num)
# OBS.: o valor final de uma range não é inclusive, portanto deve utilizar +1 ou -1 dependendo o caso.
# ----------------------------------------------------------------------------------------------------

# OUTROS EXEMPLOS:

qtd = int(input('Quantas vezes esse loop deve rodar? '))  # montando a estrutura do loop
soma = 0
for n in range(1, qtd+1):  # loop vai rodar quantas vezes informar acima
    num=int(input(f'Informe o {n}/{qtd} valor: '))
    soma=soma+num
print(f'A soma é {soma}: ')


# outro exemplo de for
nomee = 'Paulo'
for letraa in nomee:
    print(letraa)  # OBS.: no exemplo, vai imprimir uma letra abaixo da outra.

for letraa in nomee:
    print(letraa, end='')  # OBS.: aqui as letras irão imprimir uma ao lado da outra.
