import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = { 'nombre':'Eduardo','curso':'python' }
	headers = { 'Content-Type' : 'application/json', 'access-token' : '12345' }

	# response = requests.post(url,json=payload)
	response = requests.post(url,data=json.dumps(payload), headers=headers)

	# Si usamos "json", este se encarga de serializarlos
	# Si usamos "data", entonces debemos de serializarlos
	print(response.url)

	if response.status_code == 200:
		# print(response.content)
		headers_response = response.headers # Es un diccionario
		print(headers_response['Server'])