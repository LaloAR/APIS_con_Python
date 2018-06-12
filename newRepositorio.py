#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


if __name__ == '__main__':
	client_id = 'd48ab1f76b4dd8bcc379'
	client_secret = '08c25ffee67db0be06801fd39dae91fda52fd0ff'
	code = '80eb5948560e0c697481'
	access_token = '227dc725c02650c72bae90f450d4e65b14aad785'

	url = 'http://api.github.com/user/repos'
	payload = { 'name' : 'git_api_prueba' }
	headers = { 'Accept': 'application/json', 'Authorization': 'token ' + access_token }

	response = requests.post(url, headers=headers, json=payload)
	if response.status_code == 200:
		print(response.json())
	else:
		print(response.content)
