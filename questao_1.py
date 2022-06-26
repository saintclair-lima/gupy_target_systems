#QUESTÃO 01
'''Observe o trecho de código abaixo:
 	int INDICE = 13, SOMA = 0, K = 0;
 	enquanto K < INDICE faça{
		K = K + 1;
		SOMA = SOMA + K;
	}
 	imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?'''

#Opção 1: executando o algoritmo
indice, soma, k = 13, 0, 0
while k < indice:
    k += 1
    print k
    soma += k
print soma

#opção 2: abstraindo o problema
print sum(range(14))
