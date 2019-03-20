# Flask Admin PoC

Minimal instructions to run the project ('local' environment passed by
default):

```
$ python -m venv flask-poc
$ . wrg-env/bin/activate
(flask-poc) $ pip install -e .
(flask-poc) $ python app.py
```

Running tests (with code coverage):

```
$ . flask-poc/bin/activate
(flask-poc) $ pip install -e .[testing]
(flask-poc) $ py.test
...
$
```