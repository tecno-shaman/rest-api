import requests

print(requests.get('http://127.0.0.1:8080/api/jobs').json())
print(requests.get('http://127.0.0.1:8080/api/jobs/0').json())

print(requests.get('http://127.0.0.1:8080/api/jobs/99').json())
print(requests.get('http://127.0.0.1:8080/api/jobs/str').json())

print(requests.post('http://127.0.0.1:8080/api/jobs', json={'name': 'вожатый'}).json())
# пустое тело
print(requests.post('http://127.0.0.1:8080/api/jobs', json={}).json())
# нет name
print(requests.post('http://127.0.0.1:8080/api/jobs', json={'health': '80'}).json())

print(requests.get('http://127.0.0.1:8080/api/jobs').json())
