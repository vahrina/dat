import requests

r = requests.get(
    'http://natas1.natas.labs.overthewire.org',
    auth=('natas1', '0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq')
)
print(r.text)
