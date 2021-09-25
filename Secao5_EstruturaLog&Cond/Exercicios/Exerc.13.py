"""
Faça um algarítmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tem o peso 1 e a
terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para
aprovação deve ser igual ou superior a 60 pontos.

FORMULA MÉDIA PONDERADA

A*peso1 + B*peso2
---------------
 (peso1+peso2)
"""

p1 = 1
p2 = 2
prova1 = float(input('Digite a nota da 1° prova: '))
prova2 = float(input('Digite a nota da 2° prova: '))
prova3 = float(input('Digite a nota da 3° prova: '))
media = (((prova1 + prova2) * p1) + prova3 * p2) / (p1 + p2)
if media >= 60:
    print(f'A média do aluno foi de {media} pontos. Aluno aprovado')
else:
    print(f'A média do aluno foi de {media} pontos. Aluno reprovado')

