'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.'''

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
    r = valor_Total[faturamento]

    receita = f'R${r:_.6f}'
    receita = receita.replace('_','.')

    print(f'receita:{receita}')

soma = 0

for estado in valor_Total.values():
    soma = soma + estado

    valor = f'R${soma:_.6f}'
    valor = valor.replace('_','.')

print(f"\n A soma é igual: {valor}")
