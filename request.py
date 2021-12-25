import requests

url = 'https://predtempsalary.herokuapp.com/predict'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())# -*- coding: utf-8 -*-

