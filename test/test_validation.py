import unittest

from chalicelib.items import Registration
from chalicelib.validation import is_valid_registration


class TestRegistrationValidation(unittest.TestCase):

    def test_good_link(self):
        self.assertTrue(is_valid_registration(Registration(link="http://google.com/test")))

    def test_bad_host(self):
        self.assertFalse(is_valid_registration(Registration(link="/test")))

    def test_local_host(self):
        self.assertFalse(is_valid_registration(Registration(link="localhost/test")))

    def test_bad_schema(self):
        self.assertFalse(is_valid_registration(Registration(link="ws://google.com/test")))
