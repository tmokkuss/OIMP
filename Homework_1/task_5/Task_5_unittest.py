import unittest

from task_5 import *


class MyTestCase(unittest.TestCase):
    def test_check_anagrams(self):
        self.assertListEqual(check_anagrams(data=["eat", "tea", "tan", "ate", "nat", "bat"]), [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']])  # add assertion here


if __name__ == '__main__':
    unittest.main()