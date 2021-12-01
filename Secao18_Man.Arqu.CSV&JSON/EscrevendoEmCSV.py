"""
reader() = leitor
whiter() = escritor  -  Cria um objeto que permite escrever no arquivo
whiterow() = Escreve uma linha no arquivo





from csv import writer, DictWriter

#  Para criar e escrever no arquivo
#  Mesmas premissas de se trabalhar com arquivos .txt

with open('filmes.csv', 'w') as arq:
    escritor = writer(arq)
    filme = None
    escritor.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genero do filme: ')
            duracao = input('Informe a duração do filme: ')
            escritor.writerow([filme, genero, duracao])


#  Para criar, escrever e modificar arquivos .csv

#  Criando
with open('filmes.csv', 'w') as arq:  # Para modificar, trocar os "w" por "a"
    # 1° se define o cabeçalho
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    # 2° define o parâmetro dieldnames  - fieldnames é do tipo **kwargs
    escritor_csv = DictWriter(arq, fieldnames=cabecalho)
    # 3° Cria e escreve o cabeçalho
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o filme: ')
        if filme != 'sair':
            genero = input('Informe o genero: ')
            duracao = input('Informe a duração: ')
            escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duracao': duracao})
            #  As chaves devem ser, obrigatóriamente as mesmas do cabeçalho

"""
