import requests
from autenticacion import autenticacion

user = 'daquino@pam'
passwd = 'meditecEsGenial22_'
ip = '10.112.22.5'

url_usuarios = f'https://{ip}:8006/api2/json/access/users'
headers = autenticacion(user, passwd, ip)
rta = requests.get(url=url_usuarios, headers=headers, verify=False)

usuarios = rta.json()['data']

for usuario in usuarios:
	if 'firstname' in usuario:
		firstname = usuario['firstname']
	else:
		firstname = ''
	if 'lastname' in usuario:
		lastname = usuario['lastname']
	else:
		lastname = ''
	if 'email' in usuario:
		email = usuario['email']
	else:
		email = ''

	print(f'{usuario['userid']} - {firstname} - {lastname} - {email} - {usuario['enable']} - {usuario['realm-type']}')
