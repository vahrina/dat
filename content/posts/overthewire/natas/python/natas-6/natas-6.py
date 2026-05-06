import requests

with requests.Session() as s:
    s.auth = ('natas6', '0RoJwHdSKWFTYR5WuiAewauSuNaBXned')
    r = s.post(
        'http://natas6.natas.labs.overthewire.org',
        data={'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': ''}
    )

print(r.text)
