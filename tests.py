import os
import unittest

from requests_module import RequestsModule
from main import make_request, parse_response
from settings_reader import read_settings_from_json


class TestScrapingFunctions(unittest.TestCase):

    def test_settings_reader(self):
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.assertEqual(read_settings_from_json(dir_path), {"attempts": 5,
                                                             "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                                                                           " AppleWebKit/537.36 (KHTML, like Gecko) "
                                                                           "Chrome/86.0.4240.80 Safari/537.36"
                                                                           " Edg/86.0.622.48",
                                                             "url": "https://www.boredapi.com/api/activity"})

    def test_make_request(self):
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        settings = read_settings_from_json(dir_path)

        URL = settings['url']
        ATTEMPTS = settings['attempts']
        USER_AGENT = settings['user_agent']

        REQUESTS_MODULE = RequestsModule(ATTEMPTS, USER_AGENT)

        self.assertEqual(make_request(URL, REQUESTS_MODULE).status_code, 200)

    def test_parse_response(self):
        dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        settings = read_settings_from_json(dir_path)

        URL = settings['url']
        ATTEMPTS = settings['attempts']
        USER_AGENT = settings['user_agent']

        REQUESTS_MODULE = RequestsModule(ATTEMPTS, USER_AGENT)

        response = make_request(URL, REQUESTS_MODULE)
        self.assertNotEqual(parse_response(response), {})


if __name__ == '__main__':
    unittest.main()
