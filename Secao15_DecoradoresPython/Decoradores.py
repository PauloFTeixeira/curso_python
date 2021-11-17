"""
O que são decoradores:
- São funções
- Envolvem outras funções e aprimoram seu comportamento
- Também são exemplos de Higher Order Functions
- Tem uma sintaxe própria, usando o @ para chamar o decorador - Syntact Sugar(açucar sintático)


#  Exemplo

def seja_educado(funcao):
    def sendo_educado():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_educado
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

@seja_educado
def apresentando():  # A função que vai ser decorada não pode conter argumento, se conter, quebra o código
    print(f'Meu nome é Paulo')

apresentando()
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

@seja_educado
def dormir():
    print('Quero ir dormir, por favor...')

dormir()




#  Exemplo de aplicação em um site

#  Abas principais de um site
#  |  HOME  |  SERVIÇOS  |  PRODUTOS  |  ADMINISTRATIVO  |

def checa_login():  # Decorator function
    if not request.usuário:
        redirect('https//...')


def home(request):
    return 'Pode acessar home'


def servicos(request):
    return 'Pode acessar servicos'


@checa_login  # Decotador
def adm(request):
    return 'Pode acessar login'


"""
