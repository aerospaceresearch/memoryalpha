import requests
from requests.auth import HTTPBasicAuth

files = {'file': open('main.py', 'rb')}

r = requests.post('http://localhost:5000', files=files, auth=HTTPBasicAuth('admin1', 'secret1'))
print(r.status_code)