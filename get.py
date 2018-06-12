import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/get'
	args = { 'nombre':'Eduardo','curso':'python' }


	response = requests.get(url,params=args)
	print(response.url)

	if response.status_code == 200:
		# content = response.content
		# file = open('google.html','wb')
		# file.write(content)
		# file.close()
		# print(content)



		# --- Obtener json --- #
		# Forma 1
		"""
		response_json = response.json() # Diccionario
		origin = response_json['origin']
		print(origin)
		"""

		# Forma 2
		response_json = json.loads(response.text)
		origin = response_json['origin']
		print(origin)