



manipulador = open('valores_Fibo.txt', 'r')
contador = 0 
arq = open('valores_Fibo.txt', 'r')
for linha in arq:
    contador = contador + 1
print('Numero de linhas no arquivo: ', contador)
arq.close()




n = int(input('Quantos termos você quer mostrar? '))

def fib(n):

    a, b = 0, 1
    while a < n:
        print(a, end =' -- ')
        a, b = b, a + b


lista = [fib(100)]


print('\nRetornando somente as linhas que contenha a palavra')
palavra = input('Digite a palavra para buscar: ')
arq = open('valores_Fibo.txt', 'r')
contador = 0
for linha in arq:
    linha == linha.rstrip()
    if palavra in linha:
        contador == contador + 1
        print(linha)
print('\nForam retornadas', contador, 'linhas')
arq.close()



#with open('valores_Fibo.txt', 'r') as arquivo:
#    texto = arquivo.read()
 #   lista_Fibo = texto.split('\n')

  #  lista_Fibo = lista_Fibo[1:]

   # for linha in lista_Fibo:
    #    posicao_py = int(linha.find(','))

def validador(numero):
    if numero == numero:
        return True
    else:
        return False


arq = open('valores_Fibo.txt', 'r')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if '10' in linha:
        contador = contador + 1
        print(linha)