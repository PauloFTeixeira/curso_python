"""
O bloco With é usado para criar um contexto de trabaho, omde os recursos são fechados após a finalização do bloco


"""

#  Exemplo
with open('file.txt') as arq:
    print(arq.readlines())
    print(arq.closed)

print(arq.closed)

