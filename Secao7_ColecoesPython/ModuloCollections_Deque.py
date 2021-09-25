"""
Uma lista que permite a manipulação tanto no início, como também no final, nas operações de adicionar ou remover
elementos.
"""

#  Import
from collections import deque

deq = deque('Geek')
print(deq)

deq.append('P')  #  adiciona no final
print(deq)
deq.appendleft('F')  #  adiciona no começo
print(deq)

deq.pop()  #  remove o último elemento
print(deq)
deq.popleft()  #  remove o primeiro elemento
print(deq)
