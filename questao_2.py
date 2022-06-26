'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.  
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

#QUESTÃO 02
num_informado = 12586269020
num_ant = 0
num_atual = 1
eh_fibonacci = False

while num_informado >= num_atual:
    if num_informado == num_atual:
        eh_fibonacci = True
    num_ant, num_atual = num_atual, num_atual+num_ant

if eh_fibonacci:
    print '{} faz parte da sequencia fibonacci'.format(num_informado)
else:
    print '{} nao faz parte da sequencia fibonacci'.format(num_informado)
