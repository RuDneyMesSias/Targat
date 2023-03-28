'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.'''

from decimal import Decimal
import re


# Dado uma biblioteca de faturamento por estados:

valor_Total = {

    'SP': 67.83643,
    'RJ': 36.67866,
    'MG': 29.22988,
    'ES': 27.16548,
    'Outros': 19.84953

}

print('_'*85)
print('_'*85)
print('\n Faturamento por estado :\n\n {}\n'.format(valor_Total))
print('_'*85)


# Soma do faturamento por estado e dado o percentual total. 

soma = 0

for estado in valor_Total.values():
    soma = soma + estado
    valor = f'R$ {soma:_.5f}'
    receita = valor.replace('_','.')

    print( receita)
y = re.findall(r'\d+\.\d+', receita)
receita_float = float(y[0])

a = receita_float / receita_float
b = a * 100


print(f'\n A soma dos faturamento total:  R${receita_float} \n percentualmente: {b:.2f} %')
print('_'*85)
print('_'*85)


# Determinação percentual do faturamento dentre os estados de uma biblioteca 

for faturamento in valor_Total:
    pertual = valor_Total[faturamento]
    con = float(pertual)

    x = con / receita_float
    a = x * 100
    
    print(f'\n Percentualmente:  {faturamento}: {a:.2f} %')


print('_'*85)
