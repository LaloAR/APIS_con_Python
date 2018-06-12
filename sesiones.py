#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

if __name__ == '__main__':
	url = 'http://api.github.com/user'

	session = requests.session()
	session.auth = ('eduardo.alcantara.rios@outlook.com','MetallicA3006')

	response = session.get(url)
	if response.ok:
		response = session.get('https://github.com/LaloAR')
		if response.ok:
			print(response.cookies)