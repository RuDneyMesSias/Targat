'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.'''

from decimal import Decimal

valor_Total = {

    'SP': 67.83643,
    'RJ': 36.67866,
    'MG': 29.22988,
    'ES': 27.16548,
    'Outros': 19.84953

}

print('\n O faturamento total por estados listados é de :\n {}\n'.format(valor_Total))
print('_'*50)


for faturamento in valor_Total:
    pertual = valor_Total[faturamento] / 100
    
    print(f'\n faturamento dos estados é: {pertual:.2f} %')


soma = 0

for estado in valor_Total.values():
    soma = soma + estado

    valor = f'R$ {soma:_.3f}'
    valor = valor.replace('_','.')


print('_'*50)
print(f"\n somados é igual: {valor}")
print('_'*50)

