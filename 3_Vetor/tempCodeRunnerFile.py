soma = 0
re = float(valor)

for estado in valor:
    soma = soma + re
    valor = f'R$ {soma:_.2f}'
    receita = valor.replace('_','.')

    if receita == valor:
        med = receita / valor
        print(med)