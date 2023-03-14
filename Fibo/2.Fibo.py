print('_'*30)
print('Sequência de Fibonacci')

def fib(n):

    a, b = 1, 1
    while a < n:
        print(a, end ='-')
        a, b = b, a + b

lista = [fib(100000)]


print('\n')
print('_'*30)
numero = int(input('Quantos termos você quer mostrar? '))

i = 1
anterior = 1
proximo = 1

while(i < numero):
    if(i <= 1):
        next = i 
    else:
        next = anterior + proximo
        anterior = proximo
        proximo = next
        superior = anterior + proximo
    #print(next)
    i = i + 1


Faturamento = 0

with open('valores_Fibo.txt', 'r') as arquivo:
    texto = arquivo.read()
    lista_Fibo = texto.split('\n')

    lista_Fibo = lista_Fibo[1:]

    for linha in lista_Fibo:
        posicao_py = int(linha.find(','))

def validador(numero):
    if numero == numero:
        return True
    else:
        return False

lista_Fibo = list(filter(validador, lista_Fibo))
print(lista_Fibo)


if numero == anterior + superior:
    print('\n Sim! O numero {} pertence a sequencia de fibonacci '.format(next))
else:
    print('\n Não! O numero {} pertence a sequencia de fibonacci '.format(next))

print('\n O numero anterior de {} é {} e seu proximo numero é {}. '.format(next, anterior, superior))
