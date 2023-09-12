from http.cookies import SimpleCookie
import datetime, uuid
import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    cookie = SimpleCookie()
    try:
        cookie.load(req.headers['Cookie'])
        id = cookie['id'].value
    except:
        id = str(uuid.uuid4())

    expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    expires = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    return func.HttpResponse(
        body=json.dumps({
            'text': id
        }),
        status_code=200,
        headers={'Set-Cookie': 'id=' + id + '; httponly; Secure; Domain=thankful-flower-0fd4a9400.3.azurestaticapps.net; Path=/; expires=' + expires}
    )
