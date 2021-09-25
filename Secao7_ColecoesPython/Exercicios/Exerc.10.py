"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral

"""
notas = {
    'Paulo': 8.0,
    'Matheus': 9.5,
    'Eduarda': 9.5,
    'Gabriel': 8.0,
    'Eduardo': 6.85,
    'Amanda': 5.25,
    'Adao': 8.75,
    'Vanusa': 9.75,
    'Habner': 6.8,
    'Rafael': 8.0,
}

print(notas)

media = sum(notas.values())/ len(notas)
print(f'A media de notas dos alunos e {media}')

