"""
Escreva um prorgama que leia um número maior do que zero e devolva, na tela, a soma de todos os seus algarismos.
Por exemplo, ao numero 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o pragrama
terminará com a mensagem "Número inválido"
"""

numero = int(input("Informe um número inteiro"))
soma = 0
while numero > 0:
    soma += numero % 10
    numero = numero // 10
print(soma)




#  += : é equivalente a fazer x = x + valor .
#  Por exemplo, se x valer 10 e fizermos x += 2 , x passará a ter o valor 12.
#  % (Módulo): 	Retorna o resto da divisão entre operandos. EX.: 	4 % 2
#  // (Divisão inteira): Realiza a divisão entre operandos e a parte decimal do resultado 	10 // 6
