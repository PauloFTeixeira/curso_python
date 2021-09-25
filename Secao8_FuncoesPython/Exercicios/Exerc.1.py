"""
Faça uma função que receba a distância em Km e a quantidade de litros qde gasolina consumidos por um carro 
em um percurso, calcule o consumo em Km/L e escreva uma mensagem de acordo com a tabela a baixo:

CONSUMO       |         KM/L          |       MENSAGEM
------------------------------------------------------------
menor que     |        8              |     Venda o carro!

entre         |        8 e 14         |     Economico!

maior que     |        12             |     Super economica!

"""


def consumo(distância, litros):
    media = distância / litros
    print(f'A media do seu carro foi {media}')
    if media < 8:
        print('Venda o carro!')
    elif media > 8 or media < 12:
        print('Economico!')
    elif media > 14:
        print('Super economico!')
    
consumo(100, 10)



