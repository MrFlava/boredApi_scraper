import os
import unittest

from requests_module import RequestsModule
from main import make_request, parse_response, run
from settings_reader import read_settings_from_json


class TestScrapingFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        self.settings = read_settings_from_json(self.dir_path)

        self.URL = self.settings['url']
        self.ATTEMPTS = self.settings['attempts']
        self.USER_AGENT = self.settings['user_agent']

        self.requests_module = RequestsModule(self.ATTEMPTS, self.USER_AGENT)

    def test_make_request(self):
        self.assertEqual(make_request(self.URL, self.requests_module).status_code, 200)

    def test_parse_response(self):
        response = make_request(self.URL, self.requests_module)
        self.assertNotEqual(parse_response(response), {})


if __name__ == '__main__':
    unittest.main()
