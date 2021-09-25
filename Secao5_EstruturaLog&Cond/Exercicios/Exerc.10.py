"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as
seguintes fórmulas (onde h corresponde a altura)

homens (72.7 * h) - 58
mulheres (62.1 * h) - 44.7

"""
h = float(input('Qual sua altura? '))
sexo = str(input("Qual seu sexo? Digite 'F' para fenino e 'M' para masculino "))
if sexo == 'F':
    ideal = (62.1 * h) - 44.7
    print(f'Seu peso ideal é {ideal}')
elif sexo == 'M':
    ideal = (72.7 * h) - 58
    print(f'Seu peso ideal é {ideal}')

