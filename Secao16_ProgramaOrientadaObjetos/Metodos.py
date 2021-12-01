"""
Método é o mesmo que função

Representa o comportamento do objeto, as ações que ele pode realizar


#                           MÉTODO CONSTRUTOR E DE INSTANCIA
class Produto:
    #  atributo de classe
    imposto = 1.5
    #  Método construtor
    def __init__(self, nome, descricao, valor):
        #  métodos de instancia
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

    #  Método de instancia
    def abri_produto(self):
        pass
    #  Método de instancia sempre necessitam de uma instancia para funcionarem

#                           MÉTODO DE CLASSE
class Usuario:

    contador = 0

    #  Recebe o decorador classmethod
    #  Refere-se a própria classe
    #  Declarado antes do construtor
    @classmethod
    def conta_usuarios(cls):
        pass

    def __init__(self) -> None:
        pass

#  Para acessar o método de classe não se usa instancia e sim a própria classe
Usuario.conta_usuarios()
#  São usados geralmente quando não se necessita fazer acesso as instancias


#                           MÉTODO ESTÁTICO

class Usuario:

    contador = 0

    #  Recebe o decorador classmethod
    #  Refere-se a própria classe
    #  Declarado antes do construtor
    @classmethod
    def conta_usuarios(cls):
        pass

    def __init__(self) -> None:
        pass
    
    #  É uma função normal, porem dentro de uma classe
    #  Sem acesso a classe ou instancias
    @staticmethod
    def gerar_cod():
        pass

"""

