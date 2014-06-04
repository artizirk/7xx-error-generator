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

Licence
-------
WTFPL
