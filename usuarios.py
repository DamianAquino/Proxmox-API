import requests
from autenticacion import autenticacion

user = ''
passwd = ''
ip = ''

url_usuarios = f'https://{ip}:8006/api2/json/access/users'
headers = autenticacion(user, passwd, ip)
rta = requests.get(url=url_usuarios, headers=headers, verify=False)

usuarios = rta.json()['data']

for usuario in usuarios:
	firstname = usuario.get('email', '')
	lastname = usuario.get('lastname', '')
	email = usuario.get('email', '')

	print(f'{usuario['userid']} - {firstname} - {lastname} - {email} - {usuario['enable']} - {usuario['realm-type']}')
