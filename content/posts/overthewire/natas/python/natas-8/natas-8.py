import requests, base64

def dec_secret():
    """
    reverse the logic:
    bin2hex(strrev(bas64_encode(..))) -> base64_decode(strrev(hex2bin(..)))
    """
    sec = '3d3d516343746d4d6d6c315669563362'
    return base64.b64decode(bytes.fromhex(sec)[::-1]).decode()

def get_request(secret):
    with requests.Session() as s:
        s.auth = ('natas8', 'xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q')
        r = s.post(
            'http://natas8.natas.labs.overthewire.org',
            data={'secret': secret, 'submit': ''}
        )
    print(r.text)

get_request(dec_secret())
