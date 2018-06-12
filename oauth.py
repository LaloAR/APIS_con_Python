#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

client_id = 'd48ab1f76b4dd8bcc379'
client_secret = '08c25ffee67db0be06801fd39dae91fda52fd0ff'
code = '80eb5948560e0c697481'
#access_token = '227dc725c02650c72bae90f450d4e65b14aad785'


if __name__ == '__main__':
	url = 'https://github.com/login/oauth/access_token'
	payload = { 'client_id' : client_id, 'client_secret' : client_secret, 'code' : code }
	headers = { 'Accept' : 'application/json' }

	response = requests.post(url, json=payload, headers=headers)

	if response.status_code == 200:
		response_json = response.json()

		access_token = response_json['access_token']
		print(access_token)