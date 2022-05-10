import requests
import json
from urllib import parse

from config.settings.base import get_secret


def get_data():
    url = get_secret('url')
    api_key = get_secret('api_key')
    api_key_decode = parse.unquote(api_key)
    params ={
        'page' : 1,
        'perPage' : 999,
        'returnType' : 'JSON',
        'serviceKey' : api_key_decode,
    }

    response = requests.get(url, params=params)
    json_data = json.loads(response.text)
    return json_data
