import requests

print(requests.get('http://127.0.0.1:8080/api/jobs').json())

print(requests.delete('http://127.0.0.1:8080/api/jobs/2').json())

print(requests.get('http://127.0.0.1:8080/api/jobs').json())

print(requests.delete('http://127.0.0.1:8080/api/jobs/99').json())
print(requests.delete('http://127.0.0.1:8080/api/jobs/водитель').json())

print(requests.get('http://127.0.0.1:8080/api/jobs').json())
