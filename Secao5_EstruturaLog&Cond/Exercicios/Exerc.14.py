"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 a 10,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas
mensionadas anteriormente obedece aos pesos: Trabalho de laboratório: 2; Avaliação semestral: 3; Exame final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação
(entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

labor = 2
semest = 3
final = 5

notalob = int(input('Informe a nota obtida em laboratório: '))
if (notalob > 0) and (notalob <= 10):
    notasem = int(input('Informe a nota obtida no semestre: '))
    if (notasem > 0) or (notasem < 10):
        notafin = int(input('Informe a nota obtida no exame final: '))
        if (notafin > 0) or (notafin < 10):
            print('Notas recebidas')
            media = ((notalob * labor) + (notasem * semest) + (notafin * final)) // (labor + semest + final)
            if (media <= 2.9) and (media >= 0):
                print('Aluno reprovado')
            elif (media <= 4.9) and (media >= 3):
                print('Aluno em recuperação')
            else:
                print('Aluno aprovado')
else:
    print('Nota incorreta')
