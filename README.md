# Flask Admin PoC

Minimal instructions to run the project:

```
$ python -m venv flask-poc
$ . flask-poc/bin/activate
(flask-poc) $ pip install -e .
(flask-poc) $ python app.py
```

Go to http://127.0.0.1:5000/admin/ and enjoy.

Running tests (with code coverage):

```
$ . flask-poc/bin/activate
(flask-poc) $ pip install -e .[testing]
(flask-poc) $ py.test
...
$
```