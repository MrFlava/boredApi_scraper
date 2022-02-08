import os
import logging
import requests

from requests_module import RequestsModule
from settings_reader import read_settings_from_json


def make_request(url: str, requests_module) -> requests.Response:
    resp = requests_module.get_page(url)
    return resp


def parse_response(resp: requests.Response) -> dict:
    try:
        resp_json = resp.json()
        return resp_json

    except Exception as e:
        logging.error(f'parse_response: {e}')
        return {}


def run(url: str, requests_module: RequestsModule):
    response = make_request(url, requests_module)
    parse_response(response)


if __name__ == '__main__':

    dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    settings = read_settings_from_json(dir_path)

    URL = settings['url']
    ATTEMPTS = settings['attempts']
    USER_AGENT = settings['user_agent']

    REQUESTS_MODULE = RequestsModule(ATTEMPTS, USER_AGENT)

    run(URL, REQUESTS_MODULE)
