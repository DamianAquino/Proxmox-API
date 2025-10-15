import requests
from autenticacion import autenticacion
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

user = ''
passwd = ''
ip = ''

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
