from autenticacion import autenticacion
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def mostrar_discos(discos):
	for disco in discos['data']:
		print(f'{disco['storage']:<10} - {disco['enabled']} - {disco['total']:<14} - {disco['used']:<14} - {disco['avail']:<14} - {disco['type']:<4} - {disco['shared']} - {disco['active']}')

def mostrar_elementos(discos):
	print('Ingresar nombre del disco')

user = 'daquino@pam'
passwd = 'meditecEsGenial22_'
ip = '10.112.22.5'

url_nodos = f'https://{ip}:8006/api2/json/nodes'

headers = autenticacion(user, passwd, ip)

# TOMAR ID DEL NODO Y CONSTRUIR URL
response = requests.get(url_nodos, headers=headers, verify=False)
json = response.json()['data']
id = json[0]['id']
cadena = id.split('/')
id = cadena[1]

url_discos = f'https://{ip}:8006/api2/json/nodes/{id}/storage'
response = requests.get(url_discos, headers=headers, verify=False)
discos = response.json()

print('Opciones')
op = input('1 : Mostrar discos\n')
op = input('2 : Mostrar elementos\n')

if op == '1':
	mostrar_discos(discos)
if op == '2'
	mostrar_elementos(discos)

"""
for disco in discos['data']:
	print(f'{disco['storage']:<10} - {disco['enabled']} - {disco['total']:<14} - {disco['used']:<14} - {disco['avail']:<14} - {disco['type']:<4} - {disco['shared']} - {disco['active']}')
"""

for disco in discos['data']:
	url_discos = f'https://{ip}:8006/api2/json/nodes/{id}/storage/{disco['storage']}/content'
	elementos = requests.get(url_discos, headers=headers, verify=False)
	elementos = elementos.json()['data']


for elemento in elementos:
	#print(elemento['content'])
	print(f'{elemento['content']:<8}    {elemento['format']:<9}    {elemento['volid']}')
