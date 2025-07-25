import requests
from autenticacion import autenticacion

url_usuarios = f'https://{ip}:8006/api2/json/access/users'

user = ''
passwd = ''
ip = ''

# GET USUARIOS
headers = autenticacion(user, passwd, ip)
usuarios_bytes = requests.get(url=url_usuarios, headers=headers, verify=False)
usuarios = usuarios_bytes.json()['data']

for usuario in usuarios:
	firstname = usuario.get('email', '')
	lastname = usuario.get('lastname', '')
	email = usuario.get('email', '')

	print(f'{usuario['userid']} - {firstname} - {lastname} - {email} - {usuario['enable']} - {usuario['realm-type']}')
