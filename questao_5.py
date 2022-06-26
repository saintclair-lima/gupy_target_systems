'''
5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE: 
	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
	b) Evite usar funções prontas, como, por exemplo, reverse;'''
  
#QUESTÃO 05
texto_normal="Socorram-me. Subi no ônibus em Marrocos"

texto_reverso = ''

for i in range(1, len(texto_normal)+1):
    texto_reverso += texto_normal[i*(-1)]
print texto_reverso
