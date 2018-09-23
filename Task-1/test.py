#!/usr/bin/env python
import requests
import unittest

endpoint = "http://localhost:5000"


class BaseEndpoint(unittest.TestCase):
    def test(self):
        r = requests.get(endpoint+'/')
        self.assertEqual(r.status_code, 200)
