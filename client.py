import requests

files = {'file': open('main.py', 'rb')}

r = requests.post('http://localhost:5000', files=files)
print(r.status_code)