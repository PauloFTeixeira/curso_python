"""
Faça um programa que que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas
notas. Uma nota válida deve ser, obriatóriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor
válido, este fato deve ser informado ao usuário e o programa termina.
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))


if nota1 and nota2 < 0:
    print('Nota inválida')
elif nota1 and nota2 > 10:
    print('Nota inválida')
else:
    media = nota1 + nota2 / 2
    if media > 6:
        print(f'A média do aluno foi {media}, Aprovado')
    else:
        print(f'A média do aluno foi {media}, Reprovado')
