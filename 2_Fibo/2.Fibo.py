


# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 

print('_'*30)
print('Sequência de Fibonacci')

def fib(n):

    a, b = 0, 1
    while a < n:
        print(a, end ='-')
        a, b = b, a + b

lista = {
    fib(100000)
}


# Informado um número, ele calcule a sequência de Fibonacci

print('\n')
print('_'*30)
numero = int(input('Quantos termos você quer mostrar? '))

with open('valores_Fibo.txt', 'r',) as arquivo:
    texto = arquivo.read()


for Fibo in lista:
    if numero == texto:


        print('Sim!')
    else:
        print('Não!')

print(numero)
print(texto)


'''
i = 0

anterior = 0
proximo = 1

while(i < numero):
    if( i <= 1):
        next = i 
    else:
        next = anterior + proximo
        anterior = proximo
        proximo = next
        superior = anterior + proximo
        proximo = next
    print(next)
    i = i + 1

if 10 == lista:
    print(numero)
else:
    print('Não!!')'''








'''
# ele calcule a sequência de Fibonacci. 
i = 0

anterior = 0
proximo = 1

while(i < numero):
    if(i <= 1):
        next = i 
    else:
        next = anterior + proximo
        anterior = proximo
        proximo = next
        superior = anterior + proximo
    print(i)
    break
    

# E retorne uma mensagem avisando se o número informado pertence ou não a sequência.

with open('valores_Fibo.txt', 'r',) as arquivo:
    texto = arquivo.read()
print(texto.split('\n'))



for valor in texto:
    if numero == next:
        print('\n Sim! O numero {} pertence a sequencia de fibonacci '.format(numero))
else:
    print('\n Não! O numero {} pertence a sequencia de fibonacci '.format(numero))

print('\n O numero anterior de {} é {} e seu proximo numero é {}. '.format(numero, anterior, superior))'''



