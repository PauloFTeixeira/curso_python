"""
Leia um salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20%
do seu salário, imprima: Empréstimo nao consedido, caso contrário imprima: Empréstimo concedido.
"""
salario = float(input('Informe o salário: '))
prest = float(input('Informe a prestaçao que deseja pagar por mês: '))
porc = (salario / 100) * 20
if prest > porc:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
