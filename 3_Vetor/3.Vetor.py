import xml.etree.ElementTree as ET

tree = ET.parse('dados.xml')
root = tree.getroot()

id = 1 
for dia in tree.findall('dia'):
    dia.set('id', str(id))
    id += 1

tree.write('dados.xml')

