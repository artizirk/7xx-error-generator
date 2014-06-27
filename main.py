#!/usr/bin/env python3

import json
import random
import base64

html = """
<!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>HTTP ERROR {error_code} - {error_message}</title>
        <meta name="description" content="HTTP 7XX ERROR message generator">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />
        <link rel="icon" type="image/x-icon" href="favicon.ico" />
    </head>
    <body style="margin-left: 3em; margin-right:3em;">
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <br>
        <h1>HTTP ERROR {error_code}</h1>
        <p>{error_message}<!--<a href="http://arti.ee/">Go back</a>--></p>
        <hr>
        <small>Good luck!</small>
    </body>
</html>
"""

favicon = b'AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAA//8AAP//AAD//wAA//8AANudAADdawAA3vcAAO73AAD1awAAg50AAP//AAD//wAA//8AAP//AAD//wAA'

f = open("7xx-errors.json", "rb")
errors = json.loads(f.read().decode())
f.close()


def application(env, start_response):
    if env["PATH_INFO"] == "/favicon.ico":
        start_response('200 OK', [('Content-Type', 'image/x-icon')])
        return [base64.b64decode(favicon)]
    message = random.choice(errors)
    if env["PATH_INFO"] == "/json":
        start_response("200 OK", [('Content-Type', 'application/json')])
        return [json.dumps({"error_code": message[0], "error_message": message[1]}).encode()]
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html.format(error_code=message[0], error_message=message[1]).encode()]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 8080, application)
    print("Serving on http://localhost:8080/")
    httpd.serve_forever()
