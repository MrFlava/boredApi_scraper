import logging
import requests
from requests.exceptions import SSLError, InvalidURL, ConnectionError


class RequestsModule:

    def __init__(self, attempts, user_agent):
        self.attempts = attempts
        self.user_agent = user_agent

        self.headers = {
            "Accept-Language": "en",
            "User-Agent": self.user_agent
        }

    def make_request(self, method, link, data={}):

        attempts = self.attempts
        headers = self.headers if self.headers else {
            "Accept-Language": "en",
            "User-Agent": self.user_agent
        }
        cookies = {}

        while attempts > 0:
            try:
                if method == "get":
                    resp = requests.request("GET", link, data=data, headers=headers, cookies=cookies)

                else:
                    resp = requests.request("POST", link, data=data, headers=headers, cookies=cookies)
                if resp.status_code in [200]:
                    logging.debug(f"Request is successful. Status code: {resp.status_code}")

                elif resp.status_code in [403, 401, 404, 402]:
                    logging.error(f"Request is unsuccessful. Status code: {resp.status_code}")
                    raise
                return resp
            except SSLError:
                logging.error("Request is unsuccessful: unavailable site")
                continue
            except ConnectionError:
                logging.error("Request is unsuccessful: connection error")
                continue
            except InvalidURL:
                logging.error("Request is unsuccessful: invalid url")
                continue
            except Exception as e:
                logging.error(f"Request is unsuccessful: {e}")
                attempts = attempts - 1

    def get_page(self, url):
        return self.make_request('get', url)

    def post_page(self, url, data):
        return self.make_request('post', url, data)
