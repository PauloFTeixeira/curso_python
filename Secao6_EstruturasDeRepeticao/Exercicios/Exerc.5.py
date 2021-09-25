"""
Faça um programa que peça para o usuário que digite 10 valores e some-os.

qtd = int(input('Quantas vezes esse loop deve rodar? '))  # montando a estrutura do loop
soma = 0
for n in range(1, qtd+1):  # loop vai rodar quantas vezes informar acima
    num=int(input(f'Informe o {n}/{qtd} valor: '))
    soma=soma+num
print(f'A soma é {soma}: ')
"""
qtd = int(input('Digite quantas vezes desaja receber os valores: '))
soma = 0

#                     +1 porque o ultimo numero do range é não inclusive
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma} ')
