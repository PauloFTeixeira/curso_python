"""
Representam as características do objeto

Existem 3 grupos

                        ATRIBUTOS DE INSTANCIA: Declarados dentro do método construtor



class Usuario:
    def __init__(self, nome, sobrenome, email):
    #  Atributos de instancia
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
    
#     {         método construtor em ação                        }
user = Usuario('Paulo', 'Teixeira', 'agricola.teixeira@gmail.com')


#  Self refere-se ao próprio objeto em si
#  Quando se usa self.algo quer dizer:
#  o objeto tal, no atributo tal, recebe tal valor




#       ATRIBUTOS PÚCLICOS E PRIVADOS
Os atributos de instancia podem ser públicos ou privados
Isso se refere a visibilidade dos atributos
Por convenção, todo atributo é público e pode ser acessado em todo projeto


Para tornar privado, usa-se __userscore(dander) no inicio do nome
Conhecido como Name Mangling




class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

#  Para se ter acesso aos valores fora da classe, usa-se:

email = Acesso('agricola.teixeira@gmail.com', '1234')

print(email._Acesso__email)



#                               ATRIBUTOS DE CLASSE (atributos estáticos)



class Produto:
    #  atributo de classe
    imposto = 1.5
    #  Método construtor
    def __init__(self, nome, descricao, valor):
        #  métodos de instancia
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

#  Declarado diretamente na classe, geralmente iniciado com um valor, compartilhado com todas
# as instancias da classe


#                               ATRIBUTOS DINÂMICOS
#  É um atributo de instancia que pode ser criado em tempo de execução
#  Será exclusivo da instancia que o criou

p1 = Produto('arroz', 'sereal', 5,99)
#  atributo dinâmico - Exclusivo da instancia p1
p1.peso = '5Kg'

#  Para deletar um atributo
del p1.peso

"""
