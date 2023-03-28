'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:

• O menor valor de faturamento ocorrido em um dia do mês;

• O maior valor de faturamento ocorrido em um dia do mês;

• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;

b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

#Todo o texto lido em um arquivo dessa forma é uma string, mesmo que composto de dígitos. Se inteiros e números de ponto flutuante estão no texto e precisam ser usados como números, por ex. para um cálculo, eles devem ser convertidos usando-se as conversões int() e float(), respectivamente.

from decimal import Decimal

import xml.dom.minidom
import xml.etree.ElementTree as ET

mytree = ET.parse('Faturamento_Diario.xml')
myroot = mytree.getroot()

print('_'*85)
print('_'*85)
print('\n')

contador = []

for x in myroot.findall('person'):

    dia = x.find('dia').text
    valor = x.find('valor').text

    resul = float(valor)
    if resul >= 1:
        
        b = (f'R$ {resul:_.2f}')
        cont = (b.replace('_','.').replace(',','.'))
        print('O faturamento do {} foi igual: {}'.format(dia, cont))











'''
soma = 0

for group in valor:
    soma = soma + resul
    valor = f('R$ {soma:_.2f}')
    receita = float(valor.replace('_','.').replace(',','.'))    

print('_'*85)
print('_'*85)
print('\n Faturamento Total : {}\n'.format(receita))


'''
'''
soma = 0

for group in valor:
    soma = soma + re
    if soma >= 1:
        valor = f'R$ {soma:_.2f}'
        receita = (valor.replace('_','.').replace(',','.'))
        print(receita)


print('_'*85)
print('_'*85)
print('\n Faturamento Total : {}\n'.format(receita))

'''