'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction


'''# Atribuindo ID para cada dia do mês de Abril
id = 1 
for row in tree.findall('.//row'):
    row.set('id', str(id))
    id += 1
    
    # Save XML

tree.white('./dados.xml')'''


#Agora que você inicializou a árvore, você deve olhar para o XML e imprimir os valores para entender como a árvore está estruturada.

tree = ET.parse('.//dados.xml')
root = tree.getroot()

print(root)
print(root.tag)

for child in root:
    print(child.attrib, child.text)


print(root[3][1].text)








'''

for child in root:
    print(child.tag, child.attrib)

#Display classe in ET module

for (name, member) in getmembers(ET, isclass):
    if name.startswith('_'):


#Display functions in ET module

for (name, member) in getmembers(ET, isfunction):
    if name.startswith('_'):'''


'''tree = ET.parse('.//dados.xml')
root = tree.getroot()


print(root.tag)
print(root.attrib)


tree = ET.parse('dados.xml')
root = tree.getroot()
print(ET.tostring(root))'''

