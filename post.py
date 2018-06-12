import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = { 'nombre':'Eduardo','curso':'python' }


	# response = requests.post(url,json=payload)
	response = requests.post(url,data=json.dumps(payload))

	# Si usamos "json", este se encarga de serializarlos
	# Si usamos "data", entonces debemos de serializarlos
	print(response.url)

	if response.status_code == 200:
		print(response.content)