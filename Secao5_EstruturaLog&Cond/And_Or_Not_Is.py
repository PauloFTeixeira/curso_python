"""
And = e
Or = ou
Not = não
Is = é?

Operadores Unários
-Not (o valor se torna invertido, Ex se era True, com not se torna False)

Operadores Binários
-And (os dois valores tem que ser true)
-Or (um ou outro valor tem que ser true)
-Is
"""
# uso do And - os dois precisam ser True
ativo = True
logado = True
if ativo and logado:
    print('Bem vindo!')
else:
    print('Você precisa ativar sua conta')

# uso do Or - um ou outro precisam ser True
if ativo or logado:
    print('Bem vindo!')
else:
    print('Você precisa ativar sua conta')

# uso do Not - inverte o valor
if not ativo:
    print('Você precisa ativar sua conta')
else:
    print('Seja Bem vindo')

# uso do Is - um valor é comparado com o outro
if ativo is logado:  # ativo é igual a logado?
    print('Ambos ativos')
else:
    print('Não estão ativos')
