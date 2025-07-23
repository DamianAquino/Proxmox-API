import requests

def autenticacion(user, passwd, ip):
	url_ticket = f'https://{ip}:8006/api2/json/access/ticket'

	auth_data = {
		'username': user,
		'password': passwd
	}

	response = requests.post(url_ticket, data=auth_data, verify=False)
	data = response.json()['data']

	headers = {
		'Cookie': f'PVEAuthCookie={data['ticket']}',
		'CSRFPreventionToken': data['CSRFPreventionToken']
	}
	return headers
