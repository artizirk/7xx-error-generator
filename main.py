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
        <style>
        body {{
            margin: 10px auto;
            max-width: 650px;
            line-height: 1.6;
            font-size: 18px;
            color: #444;
            padding: 0 10px
        }}

        h1,h2,h3 {{
            line-height: 1.2
        }}

        hr {{
            display: block;
            height: 1px;
            border: 0;
            border-top: 1px solid #ccc;
            margin: 1em 0;
            padding: 0;
        }}
        </style>
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <h1>HTTP ERROR {error_code}</h1>
        <p>{error_message}</p>
        <hr>
        <small><a href="https://github.com/arti95/7xx-error-generator" style="color:black;">Source code</a> | <a href="/docs" style="color:black;">API Docs</a></small>,  <small>Good luck!</small>
    </body>
</html>
"""

svg = """<?xml version="1.0"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20">
<rect width="100" height="20" fill="#555"/>
<rect x="100" width="{recWidth}" height="20" fill="#4c1"/>
<rect rx="3" width="100" height="20" fill="transparent"/>
	<g fill="#fff" text-anchor="middle"
    font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
            <text x="50" y="14">HTTP ERROR {code}</text>
	    <text x="{textX}" y="14">{message}</text>
	</g>
</svg>
"""

favicon = b'AAABAAEAEBAQAAEABAAoAQAAFgAAACgAAAAQAAAAIAAAAAEABAAAAAAAgAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAA//8AAP//AAD//wAA//8AANudAADdawAA3vcAAO73AAD1awAAg50AAP//AAD//wAA//8AAP//AAD//wAA'

docs = """
<p>7xx error generator, like any other modern web service, has some API endpoints: <p>
<p><a href="/json">/json</a> endpoint for return the error in json format. <br>
<a href="/plain">/plain</a> endpoint returns the error as plain text in a single line. <br>
When accessing this website using <i>curl</i> or <a href="https://github.com/jkbrzt/httpie"><i>httpie</i></a> the error will also be returned as plain text. <br>
<a href="/html">/html</a> endpoint forces the returned error to be formated as html page.<br>
<a href="/svg">/svg</a> return a nice SVG banner that can be embeded into other html pages.</p>
"""

f = open("7xx-errors.json", "rb")
errors = json.loads(f.read().decode())
f.close()

def is_curl(user_agent):
    ua = user_agent.lower()
    return "curl" in ua or "httpie" in ua

def application(env, start_response):
    if env["PATH_INFO"] == "/favicon.ico":
        start_response('200 OK', [('Content-Type', 'image/x-icon'), ('Cache-Control', 'max-age=86400'), ('ETag', 'uwot1')])
        return [base64.b64decode(favicon)]

    if env["PATH_INFO"] == "/docs":
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return [html.format(error_code="API DOCS", error_message=docs).encode()]

    message = random.choice(errors)

    if env["PATH_INFO"] == "/json":
        start_response("200 OK", [('Content-Type', 'application/json; charset=utf-8'), ('Access-Control-Allow-Origin', '*'), ('Cache-Control', 'no-store')])
        return [json.dumps({"error_code": message[0], "error_message": message[1]}).encode()]

    if is_curl(env.get("HTTP_USER_AGENT", "")) and env["PATH_INFO"] != "/html"  or env["PATH_INFO"] == "/plain":
        start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8'), ('Access-Control-Allow-Origin', '*'), ('Cache-Control', 'no-store')])
        return ["{error_code} {error_message}\n".format(error_code=message[0], error_message=message[1]).encode()]

    if env["PATH_INFO"] == "/svg":
        start_response("200 OK", [('Content-Type', 'image/svg+xml'), ('Access-Control-Allow-Origin', '*'), ('Cache-Control', 'no-store')])
        message_len = len(message[1])
        args = {
            "width": 150,
            "recWidth": 50,
            "textX":  125,
            "code": message[0],
            "message": message[1]
        }
        if message_len > 5:
            args["width"] += 6 * (message_len)
            args["recWidth"] += 6 * (message_len)
            args["textX"] += 3 * (message_len)
        return [svg.format(**args).encode()]

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8'), ('Cache-Control', 'no-store')])
    return [html.format(error_code=message[0], error_message=message[1]).encode()]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    httpd = make_server('0.0.0.0', 8080, application)
    print("Serving on http://0.0.0.0:8080/")
    httpd.serve_forever()
