HTTP 7XX error code generator web app
=====================================
This webapp generates error pages for the new HTTP 7XX error range.
RFC for that can be found [here](https://github.com/joho/7XX-rfc)

How to run
----------
dev server can be started with just running `main.py` with `python3` command
```
$ python3 main.py
Serving on http://localhost:8080/
```
and then just open http://localhost:8080/ on your browser to be greeted
with a error page, refresh the page to get a new error. :)

For more permanent run you will probably will want to use
[uwsgi](http://uwsgi-docs.readthedocs.org/), I even included a sample
config file you can use.

Live demo server
----------------
It’s located there: http://7xx.arti.ee/

JSON API
--------
Well ofcourse it has a json api

`/json` endpoint provides random message in json format
```
‣ http GET localhost:8080/json
HTTP/1.0 200 OK
Content-Length: 48
Content-Type: application/json
Date: Fri, 27 Jun 2014 14:52:18 GMT
Server: WSGIServer/0.2 CPython/3.4.1

{
    "error_code": "723",
    "error_message": "Tricky"
}
```

and also we have a [JSONP](http://en.wikipedia.org/wiki/JSONP) enpoint at `/jsonp`
```
‣ http GET localhost:8080/jsonp?ShowMeAError
HTTP/1.0 200 OK
Content-Length: 65
Content-Type: application/javascript
Date: Fri, 27 Jun 2014 14:55:18 GMT
Server: WSGIServer/0.2 CPython/3.4.1

ShowMeError({"error_code": "741", "error_message": "Compiling"});
```

Licence
-------
WTFPL
