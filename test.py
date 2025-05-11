import requests

print(requests.get('http://127.0.0.1:8080/api/jobs').json())
print(requests.get('http://127.0.0.1:8080/api/jobs/0').json())

print(requests.get('http://127.0.0.1:8080/api/jobs/99').json())
print(requests.get('http://127.0.0.1:8080/api/jobs/str').json())


print(requests.post('http://127.0.0.1:8080/api/jobs', json={'name': 'охранник'}).json())
print(requests.get('http://127.0.0.1:8080/api/jobs').json())