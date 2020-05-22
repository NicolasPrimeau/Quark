import unittest

from chalicelib.alias import RandomAliasGenerator


class TestRandomAliasGenerator(unittest.TestCase):

    def test_good_length(self):
        gen = RandomAliasGenerator()
        self.assertEqual(10, len(gen.generate_alias(10)))
