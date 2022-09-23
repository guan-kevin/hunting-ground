import requests

# print(Buggy version 50)
print('Fixed version 50')

r = requests.get('https://google.com')
print(r.status_code)
