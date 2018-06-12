import requests

# Descargar archivos pesados

if __name__ == '__main__':
	url = 'https://i.imgur.com/n9z3sLg.jpg'

	response = requests.get(url,stream=True) # Reliza la peticion sin descargar el contenido
	with open('image.jpg','wb') as file:
		for chunk in response.iter_content(): # Descarga el contenido poco a poco
			file.write(chunk)

	response.close()