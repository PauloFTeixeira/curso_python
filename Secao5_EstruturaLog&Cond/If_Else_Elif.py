"""
If, Else e Elif

If = Se
Else = Então
Elif = Então se


"""
idade = 18
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')

# nome = 'Paulo'
# senha = 1234

nome = input('Qual seu nome? ')
if nome == 'Paulo':
    senha = input('Digite sua senha: ')
    if senha == '1234':
        print('Bem vindo ao sistema!')
else:
    print('Usuário não cadastrado ')


