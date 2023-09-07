import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({
            'test': 'こりゃまた失礼しました！'
        })
    )