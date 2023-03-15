
print('\n')
print('_'*30)
numero = int(input('Quantos termos você quer mostrar? '))

contador = 0
with open('valores_Fibo.txt', 'r',) as arquivo:
    texto = arquivo.read()
lista_texto = texto.split('\n')

for linha in lista_texto:
    posicao_pv = linha.find(';')
    contador = contador + 1


print('Numero de linhas no arquivo: ',contador)
print('Numero de linhas no arquivo: ',posicao_pv)
print('Numero de linhas no arquivo: ',lista_texto)





