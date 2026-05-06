---
date: '2026-05-05'
description: natas solved with python scripts
draft: false
title: natas/python/
---

redoing levels to discover more about socketing & i/o

i will primarily provide the source code to solve the levels;
please refer to [shell](../shell/) for thorough explanations

most scripts will follow the same scheme of issuing a `get` request with the
`auth` parameter

```py
>>> import requests, inspect
>>> print(inspect.getsource(requests.get))
def get(url, params=None, **kwargs):
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    ...
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    ...
    """
```

which could look something like this

```py
import requests

r = requests.get(
    '<url>',
    auth=('<user>', '<pass>')
)
print(r.text)
```

---

{{< natas_py >}}
