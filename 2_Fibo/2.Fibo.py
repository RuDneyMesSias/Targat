'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''


print('_'*63)
print('\n Descubra se um numero pertence ou NÃO a sequencia de Fibonacci: ')
print('_'*63)
print('_'*63)

#Entrada de um numero para validar se pertence ou não a sequencia de Fibonacci:
numero = int(input('Escolha um numero: '))
print('\n')

contador = 0 

arq = open('valores_Fibo.txt', 'r') #Importação de  (valores.txt) da sequencia 
for linha  in arq:
    contador = contador + 1
print('_'*63)

arq = open('valores_Fibo.txt', 'r') #Comparar numero apontado para validar segundo  (valores.txt) validos 
for linha in arq:
    linha = linha.rstrip()
    y = str(numero)
    if y in linha:
        if y == linha:
            print('\n Sim!!!. O numero {} pertence a sequencia de Fibonacci:\n '.format(y))
            print('_'*63)
        else:
            y != linha
            print('Não!!!. O numero {} NÃO pertence a sequencia de Fibonacci:\n'.format(y))
            print('_'*63)
        break

arq.close()

# Expressão da sequencia para validação de calculo dos  (valores.txt)
Fibo = numero + 1 
a, b = 0, 1
while a < Fibo:
    print(a, end=', ',)
    a, b = b, a + b 

print("\n Consultado nos : ", contador, "Termos") # Contador do limite dos termos validados em  (valores.txt)
