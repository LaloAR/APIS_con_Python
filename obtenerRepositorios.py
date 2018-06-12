#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

client_id = 'd48ab1f76b4dd8bcc379'
client_secret = '08c25ffee67db0be06801fd39dae91fda52fd0ff'
code = '80eb5948560e0c697481'
#access_token = '227dc725c02650c72bae90f450d4e65b14aad785'


if __name__ == '__main__':
	url = 'http://api.github.com/user/repos'
	headers =  { 'Authorization' : 'token 227dc725c02650c72bae90f450d4e65b14aad785' }

	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		payload = response.json()

		for project in payload:
			name = project['name']
			print(name)
	else:
		print(response.content)